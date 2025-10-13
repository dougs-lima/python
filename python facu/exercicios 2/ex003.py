nomes = []
for i in range(5):
    nome = input(f'Digite o nome {i+1}: ')
    nomes.append(nome)
nomes.reverse()
print('Sua lista de nome é:', nomes)
