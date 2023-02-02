def leiaint(x):
    while True:
        num = input(x).replace(' ','')
        if num == '':
            return 'O usuário não informou o número inteiro.'
        try:
            return int(num)
        except:
            print(f'O valor {num} não é inteiro!')


def leiafloat(x):
    while True:
        num = input(x).replace(' ', '')
        if num == '':
            return 'O usuário não informou o número real.'
        try:
            return float(num)
        except:
            print(f'O valor {num} não é real!')


i = leiaint('Digite um valor inteiro: ')
f = leiafloat('Digite um valor real:  ')
print('-'*30, f'\nVocê digitou:\n -> Número inteiro: {i:<10}\n -> Número real: {f:<10}')
