ano = int(input('Ano: '))
if ano%4==0 :
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')

#Jeito Arnaldo
ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or ano % 400 == 0 :
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')