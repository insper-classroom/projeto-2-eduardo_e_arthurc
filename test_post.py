import requests

url = "http://127.0.0.1:5000/imoveis/1"

data = {
    "logradouro": "Rua B",
    "tipo_logradouro": "Rua",
    "bairro": "Centro",
    "cidade": "Rio",
    "cep": "11111",
    "tipo": "apartamento",
    "valor": 200000,
    "data_aquisicao": "2025-01-01"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Texto:", response.text)