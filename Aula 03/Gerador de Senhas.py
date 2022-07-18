#Importando caracteres e biblioteca Random
import random, string

print('='*60)
#Defininido tamanho da senha que será gerado
tamanho = int(input('Insira a quantidade de caracteres que deseja em sua senha: '))

#Importando caracteres e adicionando novos, tanto letras maiúsculas e minúsculas, quanto simbolos, assim como esses especificados
chars = string.ascii_letters + string.digits + '!@#$%^&*()+=?:/'

#Sistema aleatório:
rnd = random.SystemRandom()


print("Sua senha gerada é: " + ''.join(rnd.choice(chars) for i in range(tamanho)))
print('='*60)