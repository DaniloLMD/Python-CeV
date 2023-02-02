from random import randint
from time import sleep
megasena = []
rodada = []
jogos = int(input('Quantos jogos serão sorteados: '))
for c in range(1,jogos+1):
    while True:
        num = randint(1,60)
        if num not in rodada:
            rodada.append(num)
        if len(rodada) == 6:
            break
    megasena.append(rodada[:])
    rodada.clear()
    sleep(1)
    print(f'Jogo {c}: {megasena[c-1]}')
