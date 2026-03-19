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
        "logradouro": "Rua A",
        "tipo_logradouro": "Rua",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "cep": "00000",
        "tipo": "casa",
        "valor": 100000,
        "data_aquisicao": "2024-01-01"
    }

    response = client.post("/imoveis", json=novo_imovel)

    assert response.status_code == 201
    data = response.get_json()

    assert data["tipo"] == "casa"
    assert data["cidade"] == "São Paulo"


def test_atualizar_imovel(client):
    dados = {
        "logradouro": "Rua B",
        "tipo_logradouro": "Rua",
        "bairro": "Centro",
        "cidade": "Rio",
        "cep": "11111",
        "tipo": "apartamento",
        "valor": 200000,
        "data_aquisicao": "2025-01-01"
    }

    response = client.put("/imoveis/1", json=dados)

    assert response.status_code == 200
    data = response.get_json()

    assert data["tipo"] == "apartamento"
    assert data["cidade"] == "Rio"


def test_deletar_imovel(client):
    response = client.delete("/imoveis/1")

    assert response.status_code == 204


# Filtragem de imóveis 
def test_filtrar_imoveis_por_tipo(client):
    response = client.get("/imoveis?tipo=casa")

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert all(imovel["tipo"] == "casa" for imovel in data)


def test_filtrar_imoveis_por_cidade(client):
    response = client.get("/imoveis?cidade=São Paulo")

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert all(imovel["cidade"] == "São Paulo" for imovel in data)