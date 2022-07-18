#Importando bibliotecas
from threading import Thread
import time

#Criando o objeto carro com suas caracteristicas
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto {piloto} está no Km {trajeto}\n')

#Criando thread para que ambos sejam executados ao mesmo tempo
t_carro1 = Thread(target=carro, args=[10, "Caio"])
t_carro2 = Thread(target=carro, args=[15, "Bebel"])

#Iniciando
t_carro1.start()
t_carro2.start()