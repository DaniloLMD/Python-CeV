lista = [[], []]
for c in range(1,8):
    num = int(input(f'Valor {c}: '))
    if num % 2 ==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(lista)
print(f'Pares  : {sorted(lista[0][:])}')
print(f'Impares: {sorted(lista[1][:])}')
