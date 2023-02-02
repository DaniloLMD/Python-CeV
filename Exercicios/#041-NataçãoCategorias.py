from datetime import date
ano = int(input('Ano de nascimento: '))
id = date.today().year - ano
if id <= 9 :
    print('MIRIM')
elif id <= 14 and id > 9 :
    print('INFANTIL')
elif id <= 19 and id > 14 :
    print('JUNIOR')
elif id <= 20 and id > 19 :
    print('SÊNIOR')
else :
    print('MASTER')