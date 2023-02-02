v = float(input('Velocidade do carro: '))
if v > 80.0 :
    print(f'Você será multado em {(v - 80)*7}R$')
else :
    print(f'Você está dentro do limite.')