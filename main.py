from flask import Flask, make_response, jsonify, request

from cervejas import cervejas


app = Flask(__name__)

@app.route('/busca', methods=['GET'])
def get_cerveja():
    """Responde à Solicitação GET com um JSON da nossa LISTA"""
    return make_response(
        jsonify(cervejas)
    )


@app.route('/busca', methods=['POST'])
def post_cerveja():
    """Recebe o ‘item’ a ser adicionado (JSON) e envia uma mensagem de comfirmação """
    cerveja = request.json
    cervejas.append(cerveja)
    return f'A sua {cerveja["marca"]} foi adicionada com suceso'


app.run()
