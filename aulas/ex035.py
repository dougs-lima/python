reta1 = float(input('Digite o valor da reta 1: '))
reta2 = float(input('Digite o valor da reta 2: '))
reta3 = float(input('Digite o valor da reta 3: '))
listaRetas = [reta1, reta2, reta3]
listaRetas.sort()
somaRetas = listaRetas[0] + listaRetas[1]
if somaRetas > listaRetas[2]:
    print('É possível formar triângulo com essas retas.')
else:
    print('É impossível formar um triângulo com esse essas retas.')
