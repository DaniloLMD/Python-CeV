from datetime import date
dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dic['Carteira'] = int(input('Carteira de trabalho: '))
if dic['Carteira'] > 0 :
    dic['Ano Contrato'] = int(input('Ano de contratação: '))
    dic['Salário'] = float(input('Salário: '))
    dic['Aposenta em'] = dic['Ano Contrato'] + 35
else:
    dic.pop('Carteira')
print('-=-'*30)
print(dic)
for k,v in dic.items():
    print(f'{k:<15} = {v:>20}')