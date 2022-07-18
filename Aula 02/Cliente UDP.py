#Importando a biblioteca Socket
import socket

#Criando o objeto de conexão UDP
    #Aqui foi importado o parametro SOCK_DGRAM pois o UDP é o Protocolo de Datagrama do Usuário
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client socket criado com sucesso!")

#Importado a Local Host
host = 'localhost'
porta = 5433

#Criando a mensaegem a ser enviada pelo UDP
mensagem = 'Opa server, tanquilo?'

#Tentando enviar e receber a mensagem criada acima:
try:
    #Mostrando e empacotando a mensagem, enviando naquela porta e servidor
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5433))

    #Criando variavel que receberá uma resposta do sevidor de 4096 bytes
    dados, servidor = s.recvfrom(4096)

    #Enviando a resposta, a mensagem sera desempacotada e mostrada na tela
    dados = dados.decode()
    print("Cliente: " + dados)

#Terminando, a conexão será fechada para que não fique em loop
finally:
    print("Cliente: Fechando a conexão")