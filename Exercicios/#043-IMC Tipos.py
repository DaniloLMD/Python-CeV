h = float(input('Altura: '))
p = float(input('Peso: '))
IMC = p / h**2
if IMC < 18.5 :
    print('Abaixo do peso')
elif 18.5 <= IMC < 25 :
    print('Peso Ideal')
elif 25 <= IMC < 30 :
    print('Sobrepeso')
elif 30 <= IMC < 40 :
    print('Obesidade')
else :
    print('Obesidade mórbida')