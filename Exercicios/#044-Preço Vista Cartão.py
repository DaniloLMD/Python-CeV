#CÓDIGO REFEITO
valor = float(input('Valor do produto: '))
pagamento = int(input('Método de pagamento:\n[1] À vista dinheiro/cheque\n[2] À vista cartão\n'
                      '[3] Parcelas Cartão\nEscolha: '))
if pagamento == 1 :
    print(f'Preço: RS{valor*0,9:.2f}')
elif pagamento == 2 :
    print(f'Preço: RS{valor*0,95:.2f}')
elif pagamento == 3 :
    parcelas = int(input('Número de parcelas: '))
    if parcelas <=2:
        print(f'Preço: R${valor:.2f}, com parcelas de R${valor/parcelas:.2f} cada')
    elif parcelas >=3:
        print(f'Preço: R${valor*1.2:.2f}, com parcelas de R${valor*1.2/parcelas:.2f} cada')
else:
    print('Opção inválida!')














#CÓDIGO ORIGINAL
valor = float(input('Preço do produto: '))
pagamento = int(input('[1] À vista dinheiro/cheque \n[2] À vista Cartão '
                      '\n[3] Até 2x no cartão \n[4] 3x ou mais no cartão \nPagamento: '))
if pagamento == 1 :
    print(f'Preço: R${valor*0.9:.2f}')
elif pagamento ==2 :
    print(f'Preço: R${valor*0.95:.2f}')
elif pagamento ==3 :

    print(f'Preço: R${valor} , com parcelas de R${valor/2:.2f}')
elif pagamento ==4 :
    print(f'Preço: {valor*1.2:.2f}, com parcelas de no máximo R${valor/3:.2f}')
else:
    print('Opção invalida')
