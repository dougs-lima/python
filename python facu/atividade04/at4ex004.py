precos = []
for i in range(0, 5):
    preco = float(input(f'Digite o preço {i+1}: '))
    precos.append(preco)
for j in range(0, 5):
    if precos[j] > 50:
        print(f'R${precos[j]:.2f}')
