#Uma Wordlist é um arquivo extenso de varias linhas com uma so palavra, pode ser usado pra testar a altenticação e confiabilidade de um sistema por meio de testes como o de força bruta
#Uma biblioteca de permutação e combinação: 
import itertools

#Inserindo a palavra que formará as combinaçoes
string = input("Palavra a ser permutada: ")

#Permutando a palavra com a mesma quanridade de letras que a palavra original para
resultado = itertools.permutations(string, len(string))

#Mostrando resultados
for i in resultado:
    print(''.join(i))