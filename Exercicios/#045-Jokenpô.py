#CÓDIGO REFEITO
from time import sleep
from random import randint
lista = ['Pedra','Tesoura','Papel']
eu = int(input('[1] Pedra\n[2] Tesoura\n[3] Papel\nEscolha: '))
pc = randint(1,3)
print('*-'*11+'*')
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('*-'*11+'*')
print(f'Você escolheu: {lista[eu-1]}')
print(f'PC   escolheu: {lista[pc-1]}')
if eu==pc:
    print('Empate!!!')
elif eu==1 and pc ==2 or eu ==2 and pc ==3 or eu==3 and pc ==1 :
    print('Vitória!')
else:
    print('Derrota!')
