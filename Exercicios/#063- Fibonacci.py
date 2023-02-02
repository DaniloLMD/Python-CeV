n = int(input('Termos: '))
ant = 0
at = 1
prox = 1
cont = 2
print (f'Termo 1: 0')
while cont <= n:
    print(f'Termo {cont}: {at}')
    cont += 1
    ant = at
    at = prox
    prox = at + ant