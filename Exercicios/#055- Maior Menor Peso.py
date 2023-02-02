num = int(input('Quantas pessoas: '))
print('*-'*11+'*')
if num > 0:
    peso = float(input('1o Peso: '))
    maior = peso
    menor = peso
    for c in range (2,num+1):
        peso = float(input(f'{c}o Peso: '))
        if peso > maior:
         maior = peso
        elif peso < menor:
         menor = peso
    print(f'Maior: {maior}\nMenor: {menor}')
else : 
    print('Não há pessoas!')
