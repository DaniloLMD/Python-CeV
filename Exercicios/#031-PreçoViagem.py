dist = float(input('Distância em Km: '))
if dist<= 200:
    print(f'Preço: {dist/2}R$')
else:
    print(f'Preço: {dist*0.45}R$')


