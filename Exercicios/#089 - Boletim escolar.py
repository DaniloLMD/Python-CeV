boletim = []
aluno = []
nota =[]
media = cont = 0
while True:
    aluno.append(str(input(f'Nome {cont+1}: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    media = (nota[0]+nota[1])/2
    aluno.append(nota[:])
    esc = str(input('Continuar: ')).strip().upper()[0]
    print('-=-'*20)
    boletim.append(aluno[:])
    aluno.clear()
    nota.clear()
    boletim[cont].append(media)
    cont += 1
    if esc == 'N':
        break
print(f"{'No.':<8} {'NOME':<10}      {'MÉDIA':<8}\n{'_'*60}")
for c in range(1,len(boletim)+1):
    print(f"{c:<8} {boletim[c-1][0][:][:11]:<13} {boletim[c-1][2]:>8}")
print('-=-'*20)
while True:
    esc = int(input('Ver notas de qual aluno: '))
    if esc < 1:
        break
    print(f"Notas de {boletim[esc - 1][0]} são {boletim[esc - 1][1]}")
    print('-=-'*20)

