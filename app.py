from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'titulo' : 'O morro dos ventos uivantes',
        'autor' : 'M. V. B. Souza',
    },
    {
        'id' : 2,
        'titulo' : 'Como conseguir o seu primeiro amor',
        'autor' : 'M. V. B. Souza'
    },
    {
        'id' : 3,
        'titulo' : 'O fator atitude',
        'autor' : 'J. J.'
    },
    {
        'id' : 4,
        'titulo' : 'Pai rico Pai pobre',
        'autor' : 'Julaino Jhones'
    },
    {
        'id' : 5,
        'titulo' : 'Do mil ao milhão sem cortar o cafezinho',
        'autor' : 'Thiago Nigro'
    }
]

@app.route('/')
def wellcome():
    message = 'Bem vindo, para consultar os livros adicione o endpoint /livros'
    return jsonify(message)

@app.route('/livros')
def olhar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def alterar_livros(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro =    request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port='5000',host='localhost',debug=True)