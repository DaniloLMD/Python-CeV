dic = {'Nome': '','Aproveitamento': 0}
dic['Gols'] = []
dic['Nome'] = str(input('Nome: '))
for x in range(1,int(input('Quantas partidas: '))+1):
    dic['Gols'].append(int(input(f'Gols na partida {x}: ')))
    dic['Aproveitamento'] += dic["Gols"][x-1]
print('-=-'*30)
print(dic)
print('-=-'*30)
for z,y in dic.items():
    print(f'{z:<20} = {y:}')
print('-=-'*30)
print(f'O jogador {dic["Nome"]} jogou {len(dic["Gols"])} partidas.')
for cont in range(1,len(dic["Gols"])+1):
    print(f'  -> Na partida {cont},fez {dic["Gols"][cont-1]:^5} gols.')
print(f'Totalizando {dic["Aproveitamento"]} gols.')
