n = input('Nome: ')
print(f"Em maiúsculo: {n.upper()} \n Em minúsculo: {n.lower()} \n Letras sem espaço: {len(n.replace(' ',''))} "
      f"\n Letras do primeiro nome: {len(n.split()[0])}")




#Separado
n = input('Nome: ')
print(f'Em maiúsculas: {n.upper()}')
print(f'Em minusculas: {n.lower()}')


s = n.split()
x = s[0]
y = len(x)

print('Letras do primeiro nome: ', y)
print('Letras do primeiro nome: ', len(n.split()[0]))


sem = n.replace(' ','')
tot = len(sem)
print(f'Número de letras(sem espaços): {tot}')
print(f"Número de letras(sem espaços): {len(n.replace(' ',''))}")