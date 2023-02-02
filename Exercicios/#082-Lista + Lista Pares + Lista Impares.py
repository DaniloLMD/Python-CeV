lista = []
par = []
impar = []
cont = 1
while True:
    lista.append(int(input(f'Número {cont}: ')))
    cont += 1
    esc = str(input('Deseja continuar? ')).strip().upper()[0]
    if esc == 'N':
        cont = 0
        break
while True:
    if lista[cont] % 2 == 0:
        par.append(lista[cont])
    else :
        impar.append(lista[cont])
    cont += 1
    if cont == len(lista) :
        break
print(f'Lista  original: {lista}')
print(f'Lista  Pares:    {par}')
print(f'Lista  Impares:  {impar}')

