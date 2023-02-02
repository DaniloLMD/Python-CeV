n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
print(f'Média: {(n1+n2)/2}')
if (n1+n2)/2 >= 7 :
    print('APROVADO')
elif (n1+n2)/2 < 5 :
    print('REPROVADO')
else :
    print('RECUPERAÇÃO')