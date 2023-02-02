from random import randint
cont = 0
lista = []
while True:
    qnt = int(input("Quantos números terá a lista? "))
    if qnt < 0:
        print(f'Opção inválida!')
    else:
        break
while True:
    esc = int(input('Qual número você aposta? '))
    if esc < 0 or esc > 9 :
        print(f'Opção inválida!')
    else:
      break
for c in range(0,qnt):
    lista.append(randint(0,9))
    print(f'Número {c+1}: {lista[c]}')
    if lista[c] == esc:
        cont += 1
print('-=-'*30, f'\n{lista}', f'\nEm ordem: \n{sorted(lista)}')
if esc in lista:
    print(f'Parabéns! O número {esc:^4} apareceu {cont:^3} vezes, nas posições: ',end='')
    for c in range(0,len(lista)):
        if lista[c] == esc:
            print(c+1,end='; ')
else:
    print(f'O número {esc:^5} não apareceu nenhuma vez!')