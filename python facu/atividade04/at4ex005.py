valores = []
contador = 0
total = 0
valor = True
while valor != 0:
    valor = float(input('Digite o valor do saque: '))
    valores.append(valor)
    total = total + valores[contador]
    contador += 1
print(f'O total a saque é R${total:.2f}')