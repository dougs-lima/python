class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self .nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('Au, au!')
    def correr(self):
        print(f'{self.nome} esta correndo')
cachorro_1 = Cachorros('Spike', 'Preto', 5, 'M')
cachorro_1.idade = 8
cachorro_1.latir()
cachorro_1.correr()
print(cachorro_1.nome)
print(cachorro_1.cor_de_pelo)
print(cachorro_1.idade)
print(cachorro_1.tamanho)

cachorro_2 = Cachorros('Tarzan', 'Amarelo', 4, 'G')


