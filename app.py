from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PRODUTOS = os.path.join(PASTA_PROJETO, 'inventario.json')

def ler_inventario():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []
    try:
        with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_inventario(inventario):
    with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
        json.dump(inventario, f, ensure_ascii=False, indent=4)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        # normaliza o preço: aceita vírgula ou ponto, exige pelo menos 2 casas decimais
        preco_corrigido = (request.form.get('preco', '') or '').strip().replace(',', '.')
        preco = 0.0
        if preco_corrigido:
            try:
                preco_dec = Decimal(preco_corrigido)
                # número de casas decimais
                exp = preco_dec.as_tuple().exponent
                decimal_places = -exp if exp < 0 else 0
                if decimal_places < 2:
                    preco_dec = preco_dec.quantize(Decimal('0.01'))
                preco = float(preco_dec)
            except InvalidOperation:
                preco = 0.0
        try:
            quantidade = int(request.form.get('quantidade', 0) or 0)
        except ValueError:
            quantidade = 0

        inventario = ler_inventario()
        novo_id = len(inventario) + 1

        novo_produto = {
            'id': novo_id,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }

        inventario.append(novo_produto)

        salvar_inventario(inventario)

        return redirect(url_for('cadastro'))

    return render_template('cadastro.html')


@app.route('/consulta', methods=['GET'])
def consulta():
    return render_template('consulta.html', inventario=ler_inventario())


@app.route('/pesquisar', methods=['GET'])
def pesquisar():
    # renderiza a página de pesquisa; o front-end fará consultas dinâmicas via /api/produtos
    return render_template('pesquisar.html', inventario=ler_inventario())

# API para retornar produtos filtrados por nome (query string 'q')
@app.route('/api/produtos', methods=['GET'])
def api_produtos():
    q = (request.args.get('q', '') or '').strip().lower()
    inventario = ler_inventario()
    if q:
        filtrados = [p for p in inventario if q in p.get('nome', '').lower()]
    else:
        filtrados = inventario
    return jsonify(filtrados)


if __name__ == '__main__':
    app.run(debug=True)
