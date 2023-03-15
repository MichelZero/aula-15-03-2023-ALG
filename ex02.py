#
# Autor:
# Michel Silva
# data: 15/03/2023

#
# importando o modulo requests para fazer requisições HTTP para o servidor 
import  requests as rs

# apiBrasil
# https://brasilapi.com.br/api/cep/v1/{cep}
# entrada: cep 
cep = int(input("informe o CEP: ")) # 58900000
consulta = f"https://brasilapi.com.br/api/cep/v2/{cep}" # f-string 
print(consulta) # saída da consulta https://brasilapi.com.br/api/cep/v2/58900000

requisicao = rs.get(consulta) # fazendo a requisição para o servidor da BrasilAPI e armazenando o resultado na variável requisição
print(requisicao) # teste 200 ou 404
cep1 = requisicao.json() # transformando o resultado da requisição em um dicionário
print(cep1) # printando o dicionário

