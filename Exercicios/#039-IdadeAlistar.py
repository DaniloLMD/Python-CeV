from datetime import date
nasc = int(input('Ano de nascimento: '))
if (nasc+18) > date.today().year :
    print(f'Ainda faltam {nasc+18 -date.today().year} anos para você se alistar.')
elif (nasc+18) == date.today().year :
    print('Esse ano você deve se alistar')
else :
    print(f'O ano que você deveria ter se alistado foi há {date.today().year - nasc - 18} anos')