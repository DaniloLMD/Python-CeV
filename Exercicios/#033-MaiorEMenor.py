num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo Número:  '))
num3 = float(input('Terceiro Número: '))
if num2 > num1 or num3 > num1 :
    if num3 > num2 :
      print(f'Maior: {num3}')
    else :
      print(f'Maior: {num2}')
    if num1 > num3 :
        print(f'Menor: {num3}')
    if num3 > num1 :
        print(f'Menor: {num1}')
else :
    print(f'Maior: {num1}')
    if num2 > num3 :
        print(f'Menor: {num3}')
    if num3 > num2 :
        print(f'Menor: {num2}')


#Outro Jeito
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo Número:  '))
num3 = float(input('Terceiro Número: '))
maior = num1
menor = num1
if num2 > num1 and num2 > num3 :
    maior = num2
if num2 < num1 and num2 < num3 :
    menor = num2
if num3 > num1 and num2 < num3 :
    maior = num3
if num3 < num1 and num2 > num3 :
    menor = num3
print(f'Maior: {maior} \n Menor: {menor}')