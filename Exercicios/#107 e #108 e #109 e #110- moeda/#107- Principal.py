import moeda
valor = int(input('Valor: '))
dim = float(input('Valor a ser reduzido(em %): '))
aum = float(input('Valor a ser aumentado(em %): '))
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O acréscimo de {aum} de {valor} resulta em  {moeda.aumentar(valor, aum)}')
print(f'O decréscimo de {dim} de {valor} resulta em {moeda.diminuir(valor, dim)}')


#108
valor = int(input('Valor: R$'))
dim = float(input('Valor a ser reduzido(em %): '))
aum = float(input('Valor a ser aumentado(em %): '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O acréscimo de {aum}% de {moeda.moeda(valor)} resulta em  {moeda.moeda(moeda.aumentar(valor, aum))}')
print(f'O decréscimo de {dim}% de {moeda.moeda(valor)} resulta em {moeda.moeda(moeda.diminuir(valor, dim))}')

