matriz = [[], [], []]
somapar = maiordois = 0
for c in range (1,4):
    for x in range(1,4):
        matriz[c-1].append(float(input(f'Valor {[c,x]}: ')))
        if matriz[c-1][x-1] % 2 == 0:
            somapar += matriz[c-1][x-1]
for i in range(0,3):
    for j in range (0,3):
        print(f"[{matriz[i][j]:^6}]",end=' ')
    print()
print(f'Soma dos pares: {somapar:<5,.2f}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
print(f'Soma da terceira coluna: {matriz[0][2]+matriz[1][2]+matriz[2][2]:<5,.2f}')
