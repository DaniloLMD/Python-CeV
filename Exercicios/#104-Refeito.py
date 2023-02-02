def leiaint(msg):
    while True:
        cont = 0
        num = str(input(msg)).replace(' ','')
        if len(num) == 1 and num in '0123456789':
            return num
        elif len(num) != 1:
            for valor in num:
                if valor != num[0] and valor not in '0123456789' or valor == num[0] and valor not in '-0123456789'\
                or num[0] == num[1] == '-':
                    cont += 1
        if cont == 0:
            return num
        else:
            print('Você não digitou um número inteiro!\n', '_'*20)
n = leiaint('Digite um valor inteiro: ')
print(f'Você digitou o número {n}')
