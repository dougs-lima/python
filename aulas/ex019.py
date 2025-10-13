from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
aluno = [n1, n2, n3, n4]
escolha = choice(aluno)
print(f'O aluno escolhido é {escolha}')