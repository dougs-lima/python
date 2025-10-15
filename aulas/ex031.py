distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    valorKm = distancia * 0.5
    print(f'Sua viagem vai custar R${valorKm:.2f}')
else:
    valorKm = distancia * 0.45
    print(f'Sua viagem vai custar R${valorKm:.2f}')