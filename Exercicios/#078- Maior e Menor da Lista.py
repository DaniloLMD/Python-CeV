lista = []
for c in range(1,6):
    lista.append(int(input(f'Valor {c}: ')))
print(f'Maior valor: {max(lista)} ,nas posições',end=' ')
for c in range(0,len(lista)):
    if lista[c] == max(lista):
        print(f'{c+1}', end = ' ; ')
print(f'\nMenor valor: {min(lista)} ,nas posições',end=' ')
for cc in range (0,len(lista)):
    if lista[cc] == min(lista):
        print(f'{cc+1}',end = ' ; ')
