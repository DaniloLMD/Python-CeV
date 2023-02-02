n = input('Cidade: ').upper()
print(f"Começa com Santo: {'SANTO' in (n.split()[0])}")





# Separado
n = input('Cidade:').upper()
p1 = n.split()[0]
lsant = 'SANTO' in p1
print(f'Começa com Santo: {lsant}')