import hashlib

#Criando menu de opçôes
menu = int(input(''' ###### MENU -> eSCOLHA O TIPO DE HASH DESEJADO ######
                    1. MD5
                    2. SHA1
                    3. SHA256
                    4. SHA512
    Digite o número do tipo de hash que deseja: '''))

#opçôes:
if menu == 1:
    string = input("Digite o texto que deseja converter: ")
    #Convertendo em MD5
    gerador = hashlib.md5(string.encode('utf-8'))
    print(f'O Hash MD5 da sentença "{string}" é:', gerador.hexdigest())
elif menu == 2:
    string = input("Digite o texto que deseja converter: ")
    #Convertendo em SHA1
    gerador = hashlib.sha1(string.encode('utf-8'))
    print(f'O Hash SHA1 da sentença "{string}" é:', gerador.hexdigest())
elif menu == 3:
    string = input("Digite o texto que deseja converter: ")
    #Convertendo em SHA256
    gerador = hashlib.sha256(string.encode('utf-8'))
    print(f'O Hash SHA256 da sentença "{string}" é:', gerador.hexdigest())
elif menu == 4:
    string = input("Digite o texto que deseja converter: ")
    #Convertendo em SHA512
    gerador = hashlib.sha512(string.encode('utf-8'))
    print(f'O Hash SHA512 da sentença "{string}" é:', gerador.hexdigest())
else: 
    print('Não existe essa opção')