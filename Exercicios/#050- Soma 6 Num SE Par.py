soma = 0
for c in range (0,6)
    num = int(input('Número: '))
    if num % 2 ==0 :
        soma += num
print(f'Soma dos pares = {soma}')