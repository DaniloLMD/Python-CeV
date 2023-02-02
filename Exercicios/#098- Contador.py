from time import sleep
def cont(i,f,p):
    if p == 0 :
        p = 1
    if f > i:
        for c in range(i,f+1,abs(p)):
            print(c,end=' ')
            sleep(0.2)
    else:
        if p > 0:
            for c in range(i,f-1,abs(p)*-1):
                print(c,end=' ')
                sleep(0.2)
def linha():
    print()
    print('_'*50)
cont(1, 10, 1)
linha()
cont(10, 0, 2)
linha()
inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
cont(inicio, final, passo)
