num = int(input('Número 1: '))
menor = num
maior = num
cont = 1
soma = num
res = str(input('Continuar? [S/N] '))
while res in 'Simsim' :
    cont += 1
    num = int(input(f'Número {cont}: '))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    res = str(input('Continuar? [S/N] '))
print('*-'*20+'*')
print(f'Maior: {maior}\nMenor:{menor}\nMédia:{soma/cont}')