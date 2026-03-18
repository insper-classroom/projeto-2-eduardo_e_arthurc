from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    return jsonify([]), 200

@app.route("/imoveis/<int:id>", methods=["GET"])
def buscar_imovel_por_id(id):
    return jsonify({"id": id}), 200


@app.route("/imoveis", methods=["POST"])
def adicionar_imovel():
    imovel = request.get_json()
    return jsonify(imovel), 201

@app.route("/imoveis/<int:id>", methods=["PUT"])
def atualizar_imovel(id):
    dados = request.get_json()
    dados["id"] = id
    return jsonify(dados), 200

@app.route("/imoveis/<int:id>", methods=["DELETE"])
def deletar_imovel(id):
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
