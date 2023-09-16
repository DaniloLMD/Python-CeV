from random import shuffle, choice
n1 = input('Nome do 1 aluno: ')
n2 = input('Nome do 2 aluno: ')
n3 = input('Nome do 3 aluno: ')
n4 = input('Nome do 4 aluno: ')




lista = [n1 , n2 , n3 , n4]

print(f'O aluno escolhido foi {choice(lista)}')

##EXERCICIO MEU TESTANDO LISTA ORDEM ESCOLHA GANHADOR
from random import choice
lista = str(input('Digite o nome das pessoas: '))
nome = input('Digite seu nome: ')
ordem = lista.strip().split()
ganhador = choice(ordem)
termos = len(ordem)
if nome == ganhador :
    print('Você ganhou!')
elif nome == lista[len(ordem)- 1]:
    print('Que azar! você ficou em último.')
else:
    print(f'Você ficou na posição ')
#incompleto