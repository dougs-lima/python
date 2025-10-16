cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[núm]}')
    continuar = input('Você gostaria de continuar? s ou n? ').lower()
    if continuar.startswith('n'):
        break
    if continuar != 's':
        print('Não sei bem o que quer, então vamos continuar.')
        continue