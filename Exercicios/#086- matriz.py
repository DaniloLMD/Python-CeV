matriz = [[], [], []]
for c in range (1,4):
    for x in range(1,4):
        matriz[c-1].append(float(input(f'Valor {[c,x]}: ')))
for i in range(0,3):
    for j in range (0,3):
        print(f"[{matriz[i][j]:^6}]",end=' ')
    print()
