lista = []
z = x = 0
for c in range(1,6):
    lista.append(int(input(f'Número {c}: ')))
while True:
    if lista[x] > lista[x+1]:
        z = lista[x]
        lista[x] = lista[x+1]
        lista[x+1] = z
    x += 1
    if x == 4:
        x = 0
    if lista[0] <= lista[1] <= lista[2] <= lista[3] <= lista[4] :
        break
print(lista)