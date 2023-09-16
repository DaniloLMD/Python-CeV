cond = 0
num = int(input('Número: '))
for c in range(1, num+1) :
  if num % c == 0:
    cond += 1
if cond == 2 :
    print('O número é primo')
elif num == 1 :
    print(f'O número 1 não é primo')
else:
    print('O número NÃO é primo')
print(cond)
