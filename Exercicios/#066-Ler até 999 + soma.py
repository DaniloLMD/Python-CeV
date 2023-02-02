valor = cont = soma = 0
while True:
    valor = float(input('Digite um valor: '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'Você digitou {cont} valores, e a soma entre eles é de {soma}')