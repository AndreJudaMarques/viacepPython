"""
from flask import Flask, jsonify
import requests

api = Flask(__name__)

@api.route('/')
def indice():
      cep = input('Digite o cep: ')
      dados = f'https://viacep.com.br/ws/{cep}/json/'
      requisicao = requests.get(dados)
      print(requisicao)
      print(requisicao.json())


if __name__ == '__main__':
      api.run()

#endpoint fazer requisicoes no link"""

from flask import Flask
import requests
import xmltodict

cep = input('Digite o cep: ')
dadosCep = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(dadosCep)
print('aqui', requisicao)

dicionario_requisicao = requisicao.json()
print(dicionario_requisicao) #apenas salvou o json numa biblioteca e printou 

uf = dicionario_requisicao['uf']
print(uf)

localidade = dicionario_requisicao['localidade'].lower().replace('ã', 'a').replace(' ','%20')
print(localidade)

dadosInpe = f'http://servicos.cptec.inpe.br/XML/listaCidades?city={localidade}'

requisicao2 = requests.get(dadosInpe)
print('aqui2', requisicao)

dic_inpe = requisicao2.text

print(dic_inpe)
