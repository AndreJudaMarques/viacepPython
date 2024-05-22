
from flask import Flask, jsonify
import webbrowser

api = Flask(__name__)

@api.route('/')
def indice():
      cep = input('Digite o cep: ')
      dados = f'https://viacep.com.br/ws/{cep}/json/'
      webbrowser.open(dados)
      return dados


if __name__ == '__main__':
      api.run()