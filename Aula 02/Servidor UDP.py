#Criando a biblioteca Socket
import socket

#Criando objeto de conexâo
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso')

#Criando as variaveis de host e a porta
host = 'localhost'
porta = 5432

#Criando a ligação a partir do host e da porta
s.bind((host, porta))
#Mensagem de resposta
mensagem = '\nOpa man, baum ou não?'

#Se a conexão acontecer
while 1:
    #Vai receber 4096 bytes e armazenar nessas variaveis
    dados, endereco = s.recvfrom(4096)

    #Se os dados tiverem um valor, as mensagem serão recebidas e acabou
    if dados:
        print('Servidor enviando mensagem......')
        s.sendto(dados + (mensagem.ecode()), endereco)