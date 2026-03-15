from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    return jsonify([]), 200

@app.route("/imoveis/<int:id>", methods=["GET"])
def buscar_imovel_por_id(id):
    return jsonify({"id": id}), 200


if __name__ == "__main__":
    app.run(debug=True)


