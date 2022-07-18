#Importando o Sistema Operacional e a biblioteca Time
import os
import time

#Importando o arquivo Texto e separando tudo em linhas
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

#Fazendo a verificação com 5 segundos de intevalo entre elas, por cada endereço especificado em "hosts.txt"
    for ip in dump:
        print('-'*60)
        print(f'VERIFICANDO O PI {ip}')
        os.system(f'ping -n 2 {ip}')
        time.sleep(5)
        