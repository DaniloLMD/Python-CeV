h = m18 = m20 = 0
c = 1
while True:
    idade = int(input(f'Idade P{c}: '))
    sexo = str(input(f'Sexo   P{c}: '))
    esc = str(input('Quer continuar? '))
    if sexo in 'Masculinomasculino':
        h+=1
    if idade >= 18:
        m18 +=1
    if idade < 20 and sexo in 'Femininofeminino':
        m20 += 1
    if esc in 'Simsim':
        c += 1
    elif esc in 'NaonaoNãonão':
        break
    else:
        print('Opção inválida!')
    print('~'*50)
print(f'Total: {c}\nMaiores de 18: {m18} \nHomens: {h} \nMulheres menores de 20: {m20}')
