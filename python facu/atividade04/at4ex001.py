quantidadeCamisetas = int(input('Qual a quantidade de camisetas compradas? '))
quantidadeCalcas = int(input('Qual a quantidade de calças compradas? '))

camiseta = 39.9
calca = 99.9

valorTotal = (quantidadeCamisetas * camiseta) + (quantidadeCalcas * calca)

print(f'O valor total da compra é R${valorTotal:.2f}')