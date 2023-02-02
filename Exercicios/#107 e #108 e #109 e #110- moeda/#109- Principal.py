import moeda9
show = str(input('Colocar R$? ')).strip().lower()[0]
if show == 's':
    show = True
else:
    show = False
valor = int(input('Valor: '))
dim = float(input('Valor a ser reduzido(em %): '))
aum = float(input('Valor a ser aumentado(em %): '))



print(f'O dobro de {moeda9.prefixo(valor, show)} é {moeda9.dobro(valor,show)}')
print(f'A metade de {moeda9.prefixo(valor, show)} é {moeda9.metade(valor,show)}')
print(f'O acréscimo de {aum} de {moeda9.prefixo(valor, show)} resulta em  {moeda9.aumentar(valor, aum, show)}')
print(f'O decréscimo de {dim} de {moeda9.prefixo(valor, show)} resulta em {moeda9.diminuir(valor, dim, show)}')