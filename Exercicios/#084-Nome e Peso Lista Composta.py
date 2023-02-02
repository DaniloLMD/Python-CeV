lista = []
pesados = []
leves = []
maisP = maisL = peso = cont = 0
nome = ''
while True:
    cont += 1
    nome = str(input(f'Nome {cont}: '))
    peso = float(input(f'Peso {cont}: '))
    if cont == 1:
        maisP = peso
        maisL = peso
        pesados.append(nome)
    else:
        if peso > maisP :
            maisP = peso
            pesados.clear()
            pesados.append(nome)
        elif peso < maisL:
            maisL = peso
            leves.clear()
            leves.append(nome)
        elif peso == maisP:
            pesados.append(nome)
        elif peso == maisL:
            leves.append(nome)
    esc = str(input('Continuar: ')).upper().strip()[0]
    print('~~'*25)
    if esc == 'N':
        break
print(f'Cadastros: {cont}')
print(f'Maior Peso: {maisP:<5,.2f} kg, das pessoas {pesados}')
print(f'Menor peso: {maisL:<5,.2f} kg, das pessoas {leves}')
