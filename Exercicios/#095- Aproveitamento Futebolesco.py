lista = []
while True:
    dic = {'nome': str(input('Nome: ')), 'partidas': int(input('Partidas: ')), 'gols': [], 'total': 0}
    for c in range(1, dic['partidas']+1):
        dic['gols'].append(int(input(f'Gols na partida {c}: ')))
    for c in range(0, len(dic['gols'])):
        dic['total'] += dic['gols'][c]
    esc = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    lista.append(dic.copy())
    print(f'_'*60)
    if esc == 'N':
        break
print(f'{"No.":<5} {"Nome":<10} {"Gols":<20} {"Total":>5}\n{"-=-"*20}')
for c in range(0, len(lista)):
    print(f'{c+1:<5} {lista[c]["nome"]:<10} {str(lista[c]["gols"]):<20} {lista[c]["total"]:>5}')
while True:
    esc = int(input(f'{"_"*60}\nVer jogador No.: '))
    if esc < 1 or esc > len(lista):
        break
    print(f'DADOS DO JOGADOR {lista[esc-1]["nome"]}:')
    for x in range(0, len(lista[esc-1]["gols"])):
        print(f'No jogo {x+1} fez {lista[esc-1]["gols"][x]:^5} gols.')
