#Importando as biblioetacas e a API Socket
import socket
import sys

def main():
    try:
        #Criando conexão com o socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Falha na conexão!")
        print(f'Erro: {e}')
        sys.exit()

    print("Socket foi criado com sucesso!")

    #Inserindo os dados da conexão
    hostAlvo = input('Digite o IP ou Host a ser conectado: ')
    portaAlvo =  input('Digite a porta a ser conectada: ')

    #Tebtando conexão com os dados inseridos pelo usuario pelo protocolo TCP/IP
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no host", hostAlvo, "e na porta", portaAlvo, "!")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão no host", hostAlvo, "e na porta", portaAlvo, "falhou!")
        print(f'Erro: {e}')
        sys.exit()

#Executando o Programa
if __name__ == '__main__':
    main()