
from flask import Flask
import requests

print('')
cep = input('Digite o cep: ')
dadosCep = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(dadosCep)
#print('aqui', requisicao)

dicionario_requisicao = requisicao.json()
print(dicionario_requisicao) #apenas salvou o json numa biblioteca e printou 

uf = dicionario_requisicao['uf']
#print(uf) = SP

localidade = dicionario_requisicao['localidade'] #.lower().replace('ã', 'a').replace(' ','%20')
#print(localidade) = sao%20paulo

key = 'd62f164eb8183f37dd03f6ac4eb0fcd9'

site = f'https://api.openweathermap.org/data/2.5/weather?q={localidade}&appid={key}&lang=pt_br'
req = requests.get(site)
#print('aqui2', req)

dic = req.json()
#print(dic)
tempo = dic['weather'][0]['description']
temperatura = dic['main']['temp'] - 273.15
sensacao = dic['main']['feels_like'] - 273.15
print(f'Tempo hoje = {tempo},' f' Temperatura de {temperatura:.0f}º, sensação de {sensacao:.0f}°')
print('')
print()