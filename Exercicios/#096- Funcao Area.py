print('Controle de Terrenos')
print('____________________')
def area(l, c):
    print(f'A área de um terreno {l:^5} x {c} é de {l*c:.2f}m² .')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)