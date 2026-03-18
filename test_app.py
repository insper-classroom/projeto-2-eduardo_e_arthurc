import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_listar_imoveis(client):
    response = client.get("/imoveis")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_buscar_imovel_por_id(client):
    response = client.get("/imoveis/1")

    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)


def test_adicionar_imovel(client):
    novo_imovel = {
        "id": 1,
        "tipo": "casa",
        "cidade": "São Paulo"
    }

    response = client.post("/imoveis", json=novo_imovel)

    assert response.status_code == 201
    assert response.get_json()["id"] == 1

def test_atualizar_imovel(client):
    dados = {
        "tipo": "apartamento",
        "cidade": "Rio"
    }

    response = client.put("/imoveis/1", json=dados)

    assert response.status_code == 200
    assert response.get_json()["tipo"] == "apartamento"
    assert response.get_json()["cidade"] == "Rio"


def test_deletar_imovel(client):
    response = client.delete("/imoveis/1")

    assert response.status_code == 204

