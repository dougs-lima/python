from math import hypot
co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente? '))
hi =hypot(co, ca)
print(f'A hipotenusa vale {hi:.2f}')