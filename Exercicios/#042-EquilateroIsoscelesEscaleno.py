l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print('Existe: Sim')
    if l1==l2==l3:
        print('Tipo: Equilátero')
    elif l1==l2!=l3 or l1==l3!=l2 or l3==l2!=l1:
        print('Tipo: Isósceles')
    else :
        print('Tipo: Escaleno')
else:
    print('Existe: Não')
