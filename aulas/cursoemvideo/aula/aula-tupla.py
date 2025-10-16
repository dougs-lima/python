pessoa = ('Gustavo', 39, 'M', 99.88)
print(len(pessoa))
print(pessoa)
del(pessoa)
print(pessoa) # Tuplas, como qualquer outras funções, podem ser deletadas.


"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = sorted(a + b)
print(len(c)) # Conta quantos elementos existem na tupla
print(c)
print(c.count(2)) # Conta quantas vezes aparece o valor correspondente
print(c.index(4)) # Verifica a posição do valor correspondente
print(c.index(5, 4)) # Verifica a posição do valor correspondente a partir da posição 4
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(len(lanche))
print(sorted(lanche)) # Em órdem transformando em lista, mantendo a tupla.
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
for pos, comida in enumerate(lanche):
    print(f'{pos} - Eu vou comer {comida}')
print('Comi pra caramba!')
"""


