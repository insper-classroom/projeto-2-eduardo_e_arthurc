import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_listar_imoveis_retorna_200(client):
    response = client.get("/imoveis")
    assert response.status_code == 200
    assert response.get_json() == []