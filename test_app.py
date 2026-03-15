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