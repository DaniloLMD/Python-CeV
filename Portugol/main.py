pL = float(input('Peso linguagens: '))
pR = int(input('Peso redação: '))
pH = int(input('Peso humanas: '))
pN = int(input('Peso natureza: '))
pM = int(input('Peso matemática: '))
nL = float(input('Nota linguagens: '))
nR = float(input('Nota redação: '))
nH = float(input('Nota humanas: '))
nN = float(input('Nota natureza: '))
nM = float(input('Nota matemática: '))
print(f'Resultado final: {((pL*nL + pR*nR + pH*nH + pN*nN + pM*nM)/10):.2f}')


