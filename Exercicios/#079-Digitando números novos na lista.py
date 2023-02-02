lista = []
while True:
    num = int(input('Valor: '))
    if num in lista:
        print('Valor já digitado anteriormente!')
    else:
        lista.append(num)
    esc = str(input('Deseja continuar? ')).strip().upper()[0]
    print('~~' * 25)
    if esc == 'N':
        break
print(f'A lista foi : \n{sorted(lista)}')
