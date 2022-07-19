#Importando biblioteca
import ctypes

#Definindo o que é um arquivo oculto
ocultar = 0x02

#Mudando os atributos de um arquivo
retorno = ctypes.windll.kernel32.SetFileAttributesW('Aula 05\ocultar.txt', ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Não foi ocultado")