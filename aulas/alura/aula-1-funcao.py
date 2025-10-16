def ola_mundo(nome):
    return f"Olá, {nome}!"
print(ola_mundo('Doug'))

def somar(a, b):
    soma = a + b
    return soma
soma = somar(1, 2)
print(soma)

def cumprimentar(nome = "Visitante"):
    print(f'Olá, {nome}')
cumprimentar()
cumprimentar("Sara")

def digitar_nome():
    digitar = input('Digite o seu nome: ')
    return print(digitar)
#digitar_nome()

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)
print(fatorial(4))

def taboada(n):
    print("-" * 15)
    for i in range(1,11):
        taboada = n * i
        print(f'{n} x {i} = {taboada}')
    print("-" * 15)
print(taboada(2))

def fatorial(n):
    if n ==