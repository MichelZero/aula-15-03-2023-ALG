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

