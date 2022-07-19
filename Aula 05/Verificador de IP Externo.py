#Importando bibliotecas
from itertools import count
import re
import json
from urllib.request import urlopen

#Definindo url
url = 'https://ipinfo.io/json'

#Abrindo, lendo e carregando dados
resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do seu IP:')
print(f'IP: {ip}\nProvedor: {org}\nCidade: {cidade}\nPais: {pais}\nRegião: {regiao}')
