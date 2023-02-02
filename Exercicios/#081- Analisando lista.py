lista = []
cont = 1
while True:
    lista.append(int(input(f'Número {cont}: ')))
    cont += 1
    esc = str(input('Deseja continuar? ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está dentro da lista.')
else:
    print('O número 5 NÃO está dentro da lista.')
