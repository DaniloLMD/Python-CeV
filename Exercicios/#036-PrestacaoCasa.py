valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos você pagará? '))
prest = valor / (12*anos)
if prest > 0.3*sal:
    print('O empréstimo foi negado.')
else :
    print(f'O valor da prestação mensal será de {prest}')