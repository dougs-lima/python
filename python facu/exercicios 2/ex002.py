temperatura = float(input('Qual a temperatura em celsius? '))
umidade = float(input('Qual a % de umidade? '))

if temperatura > 25 and umidade > 60:
    print('Ar quente e úmido')
elif temperatura > 25 and umidade < 60:
    print('Ar quente e seco')
elif temperatura <= 25 and umidade > 60:
    print('Ar frio e úmido')
else:
    print('Ar frio e seco')