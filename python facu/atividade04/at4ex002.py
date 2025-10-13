aluno = input('Qual o nome do aluno? ')
nota = float(input(f'Qual a nota do aluno {aluno}? '))

if nota >= 7:
    print(f'PARABÉNS! Você tirou {nota}, e foi APROVADO.')
else:
    print(f'Você foi REPROVADO, ficou abaixo do necessário')