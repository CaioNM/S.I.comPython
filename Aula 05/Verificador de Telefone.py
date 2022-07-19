#Importando bibliotecas
import phonenumbers
from phonenumbers import geocoder

#Pedindo número ao usuario e transformando string num número
numero = input('Digite o número a ser verificado no formato "+551140028922": ')
phone_numbers = phonenumbers.parse(numero)

#Mostrando a localização
print(geocoder.description_for_number(phone_numbers, 'pt'))