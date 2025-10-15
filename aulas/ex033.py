numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero2 > numero3:
    print(f'A sequência do número maior para o menor é: {numero1}, {numero2}, {numero3}')
elif numero2 > numero3 and numero3 > numero1:
    print(f'A sequência do número maior para o menor é: {numero2}, {numero3}, {numero1}')
elif numero3 > numero1 and numero1 > numero2:
    print(f'A sequência do número maior para o menor é: {numero3}, {numero1}, {numero2}')
elif numero1 > numero3 and numero3 > numero2:
    print(f'A sequência do número maior para o menor é: {numero1}, {numero3}, {numero2}')
elif numero3 > numero2 and numero2 > numero1:
    print(f'A sequência do número maior para o menor é: {numero3}, {numero2}, {numero1}')
else:
    print(f'A sequência do número maior para o menor é: {numero2}, {numero1}, {numero3}')
