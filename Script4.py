import requests

url = "https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm"

# Realiza a requisição para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Exibe o conteúdo da página
    print(response.text)
else:
    print(f"Erro ao fazer a requisição. Código de status: {response.status_code}")
