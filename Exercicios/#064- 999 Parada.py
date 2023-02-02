num = 0
soma = 0
cont = 1
while num != 999:
    num = int(input(f'Número {cont}: '))
    if num != 999:
        soma += num
        cont += 1
print (f'Você digitou {cont} números e a soma entre eles foi de {soma}')
  