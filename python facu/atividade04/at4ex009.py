pessoa1 = {
    'nome': input('Digite seu nome: '),
    'idade': int(input('Digite sua idade: ')),
}
pessoa2 = {
    'nome': input('Digite seu nome: '),
    'idade': int(input('Digite sua idade: ')),
}
pessoa3 = {
    'nome': input('Digite seu nome: '),
    'idade': int(input('Digite sua idade: ')),
}
contador = 0
listaPessoas = [pessoa1, pessoa2, pessoa3]
for pessoa in listaPessoas:
    if pessoa['idade'] > 18:
        print(f'{pessoa['nome']} é maior de 18 anos.')
        contador += 1
if contador == 0:
    print('Não tem maiores de 18 anos.')