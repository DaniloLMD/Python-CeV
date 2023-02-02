frase = str(input('Frase: ')).upper().replace(' ','')
pal = 0
inverso = ''
x = len(frase)
for c in range(0, x) :
    inverso += frase[x-1-c]
    if frase[c] == frase[x-1-c] :
        pal += 1
print(f'O inverso de {frase} é {inverso}')
if pal == x :
    print('Palindromo!')
else :
    print('Não!')

