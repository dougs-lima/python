salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    aumento = salario * 0.10
    salarioAtual = salario + aumento
    print(f'O salário vai para R${salarioAtual:.2f}')
else:
    aumento = salario * 0.15
    salarioAtual = salario + aumento
    print(f'O salário vai para R${salarioAtual:.2f}')