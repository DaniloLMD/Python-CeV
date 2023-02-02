from math import sin, cos , tan, radians,pi
a = float(input('Angulo: '))
print('_'*30)
print(f'Radianos: {(radians(a)/pi):.2f} pi rad \n Seno: {sin(radians(a)):.2f} '
      f'\n Cosseno: {cos(radians(a)):.2f} \n Tangente: {tan(radians(a)):.2f}')

print('_'*30)

ang = a*pi/180
print(f'Radianos: {(ang/pi):.3f} pi rad \n Seno: {sin(ang):.2f} \n Cosseno : {cos(ang):.2f}'
      f' \n tangente: {tan(ang):.3f}')
