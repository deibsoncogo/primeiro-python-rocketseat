import requests

url = "https://www.example.com"
response = requests.get(url)

print(f"A solicitação HTTP para {url} retornou o status {response.status_code}")
