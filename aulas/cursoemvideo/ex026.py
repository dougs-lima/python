frase = input('Digite uma frase: ').strip().upper()
print(f'A frase tem {frase.count('A')} letras "A"')
print(f'A primeira ver que aparece a letra "A" é na posição {frase.find('A') + 1}')
