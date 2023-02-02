num = int(input('Digite um número: '))
op = int(input("""Conversão: \n [1] Binário \n [2] Octal \n [3] Hexadecimal \n Escolha: """))
if op == 1 :
    print(f'O número {num} em Binário é {bin(num)[2::]}')
elif op == 2 :
    print(f'O número {num} em Octal é {oct(num)}')
elif op ==3 :
    print(f'O número {num} em Hexadecimal é {hex(num)}')
else:
    print('Burro')
