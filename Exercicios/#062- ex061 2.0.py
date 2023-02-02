t1 = float(input('Termo 1: '))
r = float(input('Razão: '))
c = 1
while c <= 10 :
    an = t1 + (c - 1) * r
    print(f'Termo {c}: {an}')
    c += 1


res = int(input('Deseja ver mais quantos termos? ')) + 10
for res in range (11, res+1):
    an = t1 + (c - 1) * r
    print(f'Termo {c}: {an}')
    c += 1