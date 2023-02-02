t = float(input('Primeiro termo: '))
r = float(input('Razão: '))
for c in range (1,11):
    print(f'{c}o termo: {(t + (c-1)*r):<3}')