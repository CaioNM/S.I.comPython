#WebCrawler é uma ferramenta de captura de informações em sites, cadastrando e salvando o que acha que seja mais relevante por meio de palavras chave

#Importa operadores matematicos
import operator
#Biblioteca de manipulação de estruturas do python
from collections import Counter
from bs4 import BeautifulSoup
import requests

def start(url):
    wordList = []
    source_code = requests.get(url).text

    #Requisita dados HTML da pagina
    soup = BeautifulSoup(source_code, 'html.parser')

    #Procura tudo que for classe e div e transforma em texto
    for each_text in soup.findAll('div', {'class': 'entry_content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordList.append(each_word)
        clean_wordList(wordList)

#Remove simbolos indesejados
def clean_wordList(wordList):
    clean_list = []
    for word in wordList:
        symbols = '!@#$%^&*()_-+={[]}|\;:"<>?/,.'
    
        for i in range(0, len(symbols)):
            #Tira o simbolo e nacoloca nada no lugar
            word = word.replace(symbols[i], '')
        if len(word)>0:
            clean_list.append(word)
    create_dictionary(clean_list)

#Passa pela lista e mostra as palavras mais repetidas
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] += 1
        
    
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("%s: %s" % (key, value))
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == "__main__":
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')