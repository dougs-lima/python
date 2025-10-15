import random

numeroAleatorio = random.randint(0, 5)
numero = int(input('Digite um número de 0 a 5: '))
if numero == numeroAleatorio:
    print(f'Parabéns, você acertou! O número é o {numeroAleatorio}')
else:
    print(f'Você errou, o número é o {numeroAleatorio}')