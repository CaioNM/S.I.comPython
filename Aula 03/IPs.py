#Importando biblioteca
import ipaddress

#Criando variaveis com valores de ip
ip = '192.168.0.1'
ip_rede = '192.168.0.0/0'

#Transformando a string em ip, tmb é capaz de manipular esses valores seguindo as regras de endereço de IP
endereco = ipaddress.ip_address(ip)
print(endereco)

#Usando um IP de rede
rede = ipaddress.ip_network(ip_rede, strict=False)
print(rede)

for ip in rede:
    print(ip)