#Importando a biblioteca do python de hash
import hashlib

#Importando dois arquivos de texto
arquivo = 'Aula 03\Arquivo1.txt'
arquivo2 = 'Aula 03\Arquivo2.txt'

#Codificando o primeiro arquivo e lendo seu conteudo
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo, 'rb').read())

#Codificando o segundo arquivo e lendo seu conteudo
hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

#Fazendo a comparaçao dos codigos Hash dos conteudos respectivos que foram gerados
if hash1.digest() != hash2.digest():
    #Se eles forem diferentes:
    print(f'O arquivo: {arquivo} é diferente do {arquivo2}')
    print(f'O Código hash do Arquivo 1 é: {hash1.hexdigest()} e o do Arquivo 2 é: {hash2.hexdigest()}')
else:
    #Se eles forem iguais
    print(f'O arquivo: {arquivo} é igual ao {arquivo2}')
    print(f'O Código hash do Arquivo 1 é: {hash1.hexdigest()} e o do Arquivo 2 é: {hash2.hexdigest()}')

#Cada código Hash é unico para uma cadeia ou caractere único