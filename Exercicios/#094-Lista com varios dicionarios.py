lista = []
dic = {}
soma = 0
while True:
    dic['nome'] = str(input('Nome     : ')).strip().capitalize()
    dic['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    dic['idade'] = int(input('Idade    : '))
    esc = str(input('Continuar[S/N]: ')).strip().upper()[0]
    lista.append(dic.copy())
    if esc == 'N':
        break
print('-=-'*30, f'\nCadastros: {len(lista)}')
for c in range(0, len(lista)):
    soma += lista[c]['idade']/len(lista)
print(f'Média: {soma}')
print(f'Mulheres cadastradas: ', end='')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(lista[c]['nome'], end='; ')
print(f'\nPessoas com idade superior à média: ')
for c in range(0, len(lista)):
    if lista[c]["idade"] >= soma:
        print(f'{lista[c]["nome"]:<7}, {lista[c]["idade"]:<3} anos, de sexo {lista[c]["sexo"]}')
