def leiaint(x):
    cont = 0
    for valor in x:
        print(valor)
        if valor == x[0] and valor not in '-0123456789':
            cont += 1
        elif valor != x[0] and valor not in '0123456789':
            cont += 1
    if cont == 0:
        return 's'
    else:
        print(f'O valor digitado não é um número inteiro!\n','_'*30)
        return 'n'


while True:
    num = leiaint(str(input('Digite um número inteiro: ')))
    if num == 's':
        break