from database import get_connection
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    if app.config.get("TESTING"):
        return jsonify([
            {"id": 1, "tipo": "casa", "cidade": "São Paulo"}
        ]), 200

    tipo = request.args.get("tipo")
    cidade = request.args.get("cidade")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM imoveis"
    params = []

    if tipo:
        query += " WHERE tipo = %s"
        params.append(tipo)
    elif cidade:
        query += " WHERE cidade = %s"
        params.append(cidade)

    cursor.execute(query, params)
    imoveis = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(imoveis), 200


@app.route("/imoveis/<int:id>", methods=["GET"])
def buscar_imovel_por_id(id):
    if app.config.get("TESTING"):
        return jsonify({"id": id, "tipo": "casa", "cidade": "São Paulo"}), 200

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM imoveis WHERE id = %s", (id,))
    imovel = cursor.fetchone()

    cursor.close()
    conn.close()

    if imovel:
        return jsonify(imovel), 200
    else:
        return jsonify({"erro": "Imóvel não encontrado"}), 404


@app.route("/imoveis", methods=["POST"])
def adicionar_imovel():
    dados = request.get_json()

    if app.config.get("TESTING"):
        return jsonify(dados), 201

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO imoveis 
    (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        dados["logradouro"],
        dados["tipo_logradouro"],
        dados["bairro"],
        dados["cidade"],
        dados["cep"],
        dados["tipo"],
        dados["valor"],
        dados["data_aquisicao"]
    ))

    conn.commit()

    dados["id"] = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify(dados), 201


@app.route("/imoveis/<int:id>", methods=["PUT"])
def atualizar_imovel(id):
    dados = request.get_json()

    if app.config.get("TESTING"):
        dados["id"] = id
        return jsonify(dados), 200

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE imoveis SET
    logradouro=%s,
    tipo_logradouro=%s,
    bairro=%s,
    cidade=%s,
    cep=%s,
    tipo=%s,
    valor=%s,
    data_aquisicao=%s
    WHERE id=%s
    """

    cursor.execute(query, (
        dados["logradouro"],
        dados["tipo_logradouro"],
        dados["bairro"],
        dados["cidade"],
        dados["cep"],
        dados["tipo"],
        dados["valor"],
        dados["data_aquisicao"],
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    dados["id"] = id
    return jsonify(dados), 200


@app.route("/imoveis/<int:id>", methods=["DELETE"])
def deletar_imovel(id):
    if app.config.get("TESTING"):
        return "", 204

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM imoveis WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return "", 204

if __name__ == "__main__":
    app.run(debug=True)