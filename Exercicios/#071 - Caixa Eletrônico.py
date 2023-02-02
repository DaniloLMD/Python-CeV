c50 = c20 = c10 = c1 = 0
print(f'''{'~~'*25}
{'BANCO DO PIR':-^50}
{'~~'*25}''')
dindin = int(input('Valor a ser sacado: R$'))
print('~~'*25)
while True:
    while dindin >= 50:
        c50 += 1
        dindin -= 50
    while dindin >= 20:
        c20 += 1
        dindin -= 20
    while dindin >= 10:
        c10 += 1
        dindin -= 10
    while dindin >= 1:
        c1 += 1
        dindin -= 1
    break
print(f'Você receberá:')
if c50 > 0:
    print(f'{c50} notas de R$50')
if c20 > 0 :
    print(f'{c20} notas de R$20')
if c10> 0 :
    print(f'{c10} notas de R$10')
if c1 > 0 :
    print(f'{c1} notas de R$1')
print('Volte sempre!')