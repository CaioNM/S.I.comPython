#Web Scraping é uma ferramenta de coleta e dados pela internet convertendo em informação estruturada para analise a quem interessar:

#Biblioteca de extração de dados HTML e XML
from bs4 import BeautifulSoup

#Biblioteca de solicitação HTML
import requests

#Site recebe o conteudo HTMl do site
site = requests.get('https://www.climatempo.com.br/').content

#Baixando o HTML do site em questao
soup = BeautifulSoup(site, 'html.parser')

#Transforma em string e exibe o html
#print(soup.prettify())

#Buscando o Titilo da pagina
print(soup.title.string)

#Procurndo a primeira tag a da pag
print(soup.a)

#Procurando algo relacionado ao adm da pag
print(soup.find('admin'))