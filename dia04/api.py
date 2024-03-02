# Importando o módulo requests, que permite fazer requisições HTTP em Python
import requests

# Definindo a URL da API que fornece informações sobre heróis
url = "https://api.opendota.com/api/heroes"

# Fazendo uma requisição GET para a URL da API e armazenando a resposta
resposta = requests.get(url)

# Verificando o código de status da resposta da requisição
resposta.status_code

# Convertendo os dados da resposta (em formato JSON) para um dicionário Python
dados = resposta.json()
# Os dados são uma lista de dicionários, onde cada dicionário representa um herói

# Acessando as informações sobre os papéis de um herói específico
dados[0]['roles']

# Iterando sobre todos os heróis na lista de dados
for i in dados:
    # Imprimindo o nome localizado de cada herói
    print(i['localized_name'])
