from flask import Flask, render_template, request, redirect, url_for
import json
import os

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

@app.route('/', methods=['GET', 'POST'])
def adicionar():

    nome = request.form['nome']
    preco = float(request.form['preco'])
    quantidade = int(request.form['quantidade'])

    if request.method == 'POST':
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

        return redirect(url_for('adicionar'))
    
    return render_template('index.html')
