tupla = ('arnaldo', 'geraldo', 'aza', 'pyr')
v = 0
for c in range(0 , len(tupla)):
    print(f'Vogais em {tupla[c]}: ',end='')
    for x in range (0,len(tupla[c])):
        if tupla[c][x] in 'aeiouAEIOU':
            print(tupla[c][x],end=' ')
            v += 1
        if x == (len(tupla[c]) -1):
            if v == 0:
                print('Não há vogais!')
    print('\n')
    v = 0
