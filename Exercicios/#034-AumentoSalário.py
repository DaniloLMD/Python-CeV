sal = float(input('Salário: '))
if sal <= 1250 :
    print(f'Após o aumento: R${sal*1.15:.2f}')
else:
    print(f'Após o aumento: R${sal*1.1:.2f}')