num = float(input('Número: '))
for c in range (0,11):
    print(f'{num:>5} x {c:>2} = {num*c:>3,.2f}')
