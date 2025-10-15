velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa:.2f} por excesso de velocidade. A velocidade da via era de 80km/h, você ultrapassou com {velocidade}km/h')