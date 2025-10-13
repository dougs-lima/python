numero = int(input('Digite um número: '))

if numero < 0:
    print(f'O número {numero} é negativo.')
elif numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é impar.')