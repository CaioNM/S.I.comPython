#Importando o OS para o python
import os

print("#" *60)

#Inserindo o IP a ser verificado
ipHost = input("Digite o IP ou o Host que deseja verificar: ")
#Usndo o comando ping do sistema operacional para verificar a conectividade enviando 4 pacotes
os.system(f'ping -n 4 {ipHost}')

print('-'*60)