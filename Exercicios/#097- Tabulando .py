nome = ''
def escreva(n):
    print('_'* (len(n)+4))
    print(f'  {n}  ')
    print('_' * (len(n)+4))
while nome != 0:
    nome = str(input('\nNome: '))
    escreva(nome)

