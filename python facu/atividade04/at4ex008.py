produto1 = {
    'nome': 'Cereal',
    'preço': 11.9
}
produto2 = {
    'nome': 'Bolacha',
    'preço': 4
}
produto3 = {
    'nome': 'Chocolate',
    'preço': 5.5
}
pesquisa = input('Qual o produto? ')
listaProdutos = [produto1, produto2, produto3]
for produto in listaProdutos:
    if produto['nome'] == pesquisa:
        print(f'R${produto['preço']:.2f}')
        break
if produto['nome'] != pesquisa:
    print('Produto inexistente')