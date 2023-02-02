num1 = 0
num2 = 0
escolha = 0
while escolha != 5:
    num1 = float(input('Número 1: '))
    num2 = float(input('Número 2: '))
    escolha = int(input('[1]Somar          [2]Multiplicar\n         [3]Maior\n[4]Novos          [5]Sair\n\nEscolha: '))
    if escolha == 1:
        print(f'{num1:.2f} + {num2:.2f} = {num1+num2:.2f,<5}')
    elif escolha ==2:
        print(f'{num1} x {num2} = {num1*num2:<5,.2f}')
    elif escolha ==3:
        if num1 > num2:
            print(f'O maior é {num1}')
        if num1 == num2:
            print(f'Os dois são iguais!')
        else:
         print(f'O maior é {num2}')
    elif escolha == 4 :
        print('Recomeçando...')
    else:
        print('Adeus')