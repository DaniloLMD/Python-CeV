p = int(input('Quantas pessoas: '))
print('*-'*21+'*')
mm = 0
iv = 0
if p > 0:
    nome  = str(input('Nome  P1      : '))
    idade = int(input('Idade P1      : '))
    sexo  = str(input('Sexo  P1 [F/M]: ')).upper()
    print('_'*43)
    si = idade
    if sexo == 'M' :
        hv = nome
        iv = idade
    else:
        hv = 'Não há homens!'
    if sexo == 'F' and idade < 20 :
        mm += 1
    for c in range (2,p+1):
        nome  = str(input(f'Nome  P{c}      : '))
        idade = int(input(f'Idade P{c}      : '))
        sexo  = str(input(f'Sexo  P{c} [F/M]: ')).upper()
        print('_'*43)
        si += idade
        if sexo == 'M' and (idade > iv) :
            hv = nome
            iv = idade
        if sexo == 'F' and idade < 20:
            mm += 1
    print('*-'*21+'*')
    print(f'Média de idade do grupo: {si/p:.2f}\nHomem mais velho: {hv}\nMulheres abaixo de 20 anos: {mm}')
else:
    print('Não há pessoas!')
