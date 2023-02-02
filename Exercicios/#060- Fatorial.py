num = int(input('Número: '))
fat = 1
for c in range (num, 0, -1):
    print(f'{c}', end=" ")
    fat = fat*c
    if c > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
print (f'{fat}')

#WHILE
num = int(input('Número: '))
fat = 1
while num > 0 :
    print(f'{num}' , end=' ')
    if num > 1:
        print('x', end = ' ')
    else:
        print('=', end =' ')
    fat = fat*num
    num = num-1
print(f'{fat}')