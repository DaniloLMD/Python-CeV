tot = maior = menor = mil = 0
c = 2
produto = str(input(f'Produto 1: '))
preço = float(input(f'Preço  P1: '))
maior = menor = preço
nomeMa = nomeMe = produto
nomeMa = nomeMe = ''
esc = str(input('Deseja continuar? '))
print('~~'*25)
while esc in 'Simsim':
    produto = str(input(f'Produto {c}: '))
    preço = float(input(f'Preço  P{c}: '))
    tot += preço
    if preço >= 1000:
        mil += 1
    if preço > maior :
        maior = preço
        nomeMa = produto
    elif preço < menor :
        menor = preço
        nomeMe = produto
    esc = str(input(('Deseja continuar? ')))
    if esc in 'Simsim':
        c += 1
    elif esc in 'NãonãoNaonao':
        break
    else:
        print('Opção inválida!')
    print('~~'*25)
print(f'Total: R${tot} \nProdutos comprados: {c} \nMais barato: {nomeMe}, R${menor} \nMais   caro: {nomeMa}, R${maior}\nCustaram mais de R$1000: {mil} produtos.')
