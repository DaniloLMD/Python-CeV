from random import randint
num = int(input('Tente adivinhar um número de 0 a 5: '))
numpc = randint(0,5)
if num==numpc :
    print('Você acertou!')
else:
    print(f'Você errou! O número era {numpc}')
