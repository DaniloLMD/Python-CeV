from random import randint
dic = {'Jogadores': [], 'Valores': []}
jogtemp = ''
valtemp = 0
for c in range(0,4):
    dic["Jogadores"].append(str(input(f'Jogador {c+1}: ')))
for c in range (1,5):
    dic["Valores"].append(randint(1,6))
    print(f'{dic["Jogadores"][c-1]:<10} tirou {dic["Valores"][c-1]:>5}')
while True:
    for c in range (0,3):
        if dic["Valores"][c] < dic["Valores"][c+1]:
            valtemp = dic["Valores"][c]
            dic["Valores"][c] = dic["Valores"][c+1]
            dic["Valores"][c+1] = valtemp
            jogtemp = dic["Jogadores"][c]
            dic["Jogadores"][c] = dic["Jogadores"][c+1]
            dic["Jogadores"][c+1] = jogtemp
    if dic["Valores"][0] >= dic["Valores"][1] >= dic["Valores"][2] >= dic["Valores"][3]:
        break
for c in range(0,4):
    print(f'-> {c+1}o lugar: {dic["Jogadores"][c]:<10}, com o valor de {dic["Valores"][c]:<2}')
