n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
n4 = int(input('Número 4: '))
tupla = (n1,n2,n3,n4)
print(f'Quantas vezes aparece 9: {tupla.count(9)}')
print(f'Posição do primeiro 3: {tupla.index(3)+1}') if 3 in tupla else print('Posição do primeiro 3: Não há.')
print('Pares: ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ; ') 