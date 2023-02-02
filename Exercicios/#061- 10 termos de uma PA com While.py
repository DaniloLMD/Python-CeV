t1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
c = 1
while c <= 10:
    print(f'Termo {c}: {t1+(c-1)*r:<5}')
    c += 1
