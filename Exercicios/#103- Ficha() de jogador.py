def ficha(n, g='0'):
    if g in '0123456789':
        if len(n) == 0:
            n = '<desconhecido>'
        if len(g) == 0:
            g = 0
        print(f'O jogador {n} fez {g} gols.')
    else:
        print('Número de gols errado!')

nome = str(input('Nome: ')).strip()
gols = str(input('Gols: '))
ficha(nome, gols)
