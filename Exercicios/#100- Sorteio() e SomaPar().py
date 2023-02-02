from random import randint
lista = []
def sortear(mst):
    for c in range(0,5):
        mst.append(randint(1,10))
    print(f'Valores sorteados: {str(mst):>15}')
def somaPar(oi):
    sp = 0
    for v in oi:
        if v % 2 ==0 :
            sp += v
    print(f'Soma dos pares   : {sp:<15}')
sortear(lista)
somaPar(lista)
