# Inventário (Projeto Web II)

Aplicação web educativa para gerenciamento básico de inventário; indicada para fins acadêmicos e demonstração.

## Visão geral

Aplicação em Python (Flask) que permite cadastrar, visualizar e pesquisar itens de inventário. Os dados são armazenados localmente em `inventario.json` como um arquivo JSON simples — ideal para exercícios e protótipos.

## Tecnologias

- Python 3.8+
- Flask (ver `requirements.txt`)

## Instalação

1. Criar e ativar ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

## Execução

Você pode executar a aplicação diretamente ou via CLI do Flask:

```bash
# execução direta (se `app.py` contém o bloco "if __name__ == '__main__'")
python app.py

# ou (opcional) com o flask CLI
export FLASK_APP=app.py
flask run --host=127.0.0.1 --port=5000
```

Abra http://localhost:5000 no navegador.

## Rotas e uso

- `/` — lista de itens e página inicial.
- `/cadastro` — formulário para adicionar novo item (campos típicos: nome, quantidade, descrição, local).
- `/consulta` — visualização detalhada de um item.
- `/pesquisar` — formulário/endpoint para buscar por nome ou atributos.

Use o formulário em `/cadastro` para inserir novos registros; os dados serão gravados em `inventario.json`.

## Formato do arquivo de dados

O arquivo `inventario.json` armazena uma lista de objetos; exemplo de estrutura:

```json
[
  {
    "id": 1,
    "nome": "Teclado",
    "quantidade": 10,
    "descricao": "Teclado mecânico",
    "local": "Sala 101",
    "data_aquisicao": "2024-03-10"
  }
]
```

Para repor o inventário manualmente, edite ou substitua `inventario.json` com uma estrutura compatível.

## Boas práticas e limitações

- Destinado apenas a fins acadêmicos; não use em produção sem melhorias.
- Limitações: sem autenticação, sem backup, sem concorrência para múltiplos usuários.
- Sugestões para evolução: migrar para banco de dados (SQLite/Postgres), validar entradas do usuário, adicionar autenticação e testes automatizados.

## Organização do repositório

- `app.py` — aplicação Flask principal
- `inventario.json` — armazenamento JSON local
- `requirements.txt` — lista de dependências
- `templates/` — templates HTML (`index.html`, `cadastro.html`, `consulta.html`, `pesquisar.html`)

## Como contribuir / testar

- Para testar rapidamente, ative o ambiente, instale dependências e execute `python app.py`.
- Para resetar os dados, remova ou renomeie `inventario.json` e crie um novo com a estrutura acima.

## Observação final

Projeto criado para estudo. Use apenas em ambiente local e como referência didática.

Autor: aluno (uso acadêmico)
