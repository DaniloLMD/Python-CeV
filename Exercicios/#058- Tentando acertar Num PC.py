from random import randint
jog = int(input('Número entre 1 e 10: '))
pc = randint(1,10)
tent = 1
while jog != pc:
    if jog < pc :
        print('Maior....')
    else :
        print('Menor...')
    jog = int(input(f'Você errou! Tente denovo: '))
    print('~'*50)
    tent += 1



print(f'Você acertou, com um total de {tent} tentativas.')
if tent == 1:
    print('De primeira, parabéns!!!!')
