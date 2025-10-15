dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
dias = dias * 60
km = km * 0.15
total = dias + km
print(f'Total a pagar no aluguel do carro é R${total:.2f}')