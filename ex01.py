#
# Autor:
# Michel Silva
# data: 15/03/2023

#
# importando o modulo requests para fazer requisições HTTP para o servidor 
import  requests as rs

# fazendo a requisição para o servidor da BrasilAPI e armazenando o resultado na variável requisição
requisicao = rs.get('https://brasilapi.com.br/api/cep/v2/58900000')

# imprimindo o resultado da requisição para o servidor da BrasilAPI
print(requisicao) # teste 200 ou 404 
cep1 = requisicao.json() # transformando o resultado da requisição em um dicionário
print(cep1) # printando o dicionário

# saída
# <Response [200]>
# {'cep': '58900000', 'state': 'PB', 'city': 'Cajazeiras', 'service': 'correios', 'location': {'type': 'Point', 'coordinates': {}}}