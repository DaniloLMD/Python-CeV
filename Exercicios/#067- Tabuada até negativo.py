while True:
    num = int(input('Número: '))
    if num < 0:
        break
    for c in range (1,11) :
        print(f'{num} x {c} = {num*c:<10}')
    print('~'*50)

print('Fim')