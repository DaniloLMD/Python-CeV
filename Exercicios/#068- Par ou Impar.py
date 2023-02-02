vit = 0
x = ''
from random import randint
while True:
    esc = str(input('Par ou impar? '))
    num = int(input('Valor: '))
    pc = randint(0,5)
    res = num + pc
    if res % 2 == 0:
        x = 'Par'
    else:
        x = 'Impar'
    print(f'PC escolheu {pc}, resultando em {x}')
    print('~' * 50)
    if esc not in 'ParparImparimpar':
        print('Opção inválida!')
    elif esc in 'Parpar' and res%2 == 0 or esc in 'Imparimpar' and res%2 != 0:
        vit += 1
    else:
        break
print(f'Você alcançou {vit} vitórias consecutivas!')
