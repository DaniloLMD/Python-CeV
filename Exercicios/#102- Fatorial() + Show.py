
def fatorial(x):
    fat = 1
    for c in range(x, 0, -1):
        fat *= c
        if show=='s':
            if c > 1:
                print(f'{c} x ',end='')
            else:
                 print(f'{c} = {fat}')
        elif (c == 1):
           print(f'Resultado: {fat}')

num = int(input('Número: '))
show = str(input('Showzinho? ')).strip().lower()[0]
fatorial(num)
