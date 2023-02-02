l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print('É possível formar esse triângulo')
else :
    print('Não é possível formar esse triângulo')
