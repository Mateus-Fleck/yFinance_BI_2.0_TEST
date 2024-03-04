import requests
from bs4 import BeautifulSoup

url = "https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm"

# Realiza a requisição para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Parseia o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar os elementos que contêm os nomes dos bancos (ajuste conforme a estrutura HTML da página)
    # Exemplo: se os nomes dos bancos estão em tags <div> com a classe "nome-banco", pode ser algo como:
    banco_elements = soup.find_all('div', class_='nome-banco')

    # Exibir os nomes dos bancos encontrados
    for banco_element in banco_elements:
        print(banco_element.text.strip())
else:
    print(f"Erro ao fazer a requisição. Código de status: {response.status_code}")
