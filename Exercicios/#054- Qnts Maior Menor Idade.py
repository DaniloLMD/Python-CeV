from datetime import date
maior = 0
menor = 0
for c in range (1,8) :
    p = int(input(f'{c}o ano de nascimento: '))
    if (date.today().year - p) >= 21 :
        maior += 1
    else :
        menor += 1
print('*-'*11+'*')
print(f'Maiores: {maior} \nMenores: {menor}')