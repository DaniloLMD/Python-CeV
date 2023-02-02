#Em valores
def mais(*num):
    print(f'O maior de {num} é {max(num)}')
mais(0, 5, 15, 69, 20, 30)





#Em listas
def maior(dst):
    print(f'O maior é: {max(dst)}')
lista = []
c = 0
while True:
    c += 1
    esc = int(input(f'Número {c}: '))
    if esc == 0:
        break
    lista.append(esc)
maior(lista)
