listafinal = []
lista = []
leve = pesado = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    esc = str(input('Continuar: ')).strip().upper()[0]
    print('-=-'*15)
    listafinal.append(lista[:])
    if len(listafinal) == 1:
        pesado = listafinal[0][1]
        leve = listafinal[0][1]
    else:
        if lista[1] >= pesado:
            pesado = lista[1]
        elif lista[1] <= leve:
            leve = lista[1]
    lista.clear()
    if esc == 'N':
        break
print(listafinal)
print(f'Cadastros: {len(listafinal)}')
print(f'Mais pesado: {pesado:<5,.2f} kg. Nome(s): ', end='')
for x in range(0, len(listafinal)):
    if listafinal[x][1] == pesado:
        print(listafinal[x][0], end='; ')
print(f'\nMais leve  : {leve:<6,.2f} kg. Nome(s): ', end='')
for y in range(0, len(listafinal)):
    if listafinal[y][1] == leve:
        print(listafinal[y][0], end='; ')
