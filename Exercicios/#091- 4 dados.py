from random import randint
dic = {}
jog = []
jogtemp = []
z = 0
for c in range (1,5):
    dic[c] = randint(1,6)
    print(f'Jogador {c} tirou {dic[c]}')
    jogtemp.append(f'Jogador {c} ')
    jogtemp.append(dic[c])
    jog.append(jogtemp[:])
    jogtemp.clear()
while True:
    for x in range (1,4):
        if dic[x] > dic[x+1]:
            z = dic[x]
            dic[x] = dic[x+1]
            dic[x+1] = z
    if dic[1] <= dic[2] <= dic[3] <= dic[4]:
        break
for c in range(1,5):
    print(f'{c}o lugar: {dic[5-c]}, do jogador ',end='')
    if dic[5-c] == jog[0][1]:
        print(jog[0][0],end='; ')
        if dic[5-c] == jog[1][1]:
            print(jog[1][0])
        elif dic[5-c] == jog[2][1]:
            print(jog[2][0])
        elif dic[5-c] == jog[3][1]:
            print(jog[3][0])
    elif dic[5-c] == jog[1][1]:
        print(jog[1][0],end='; ')
        if dic[5-c] == jog[0][1]:
            print(jog[0][0])
        elif dic[5-c] == jog[2][1]:
            print(jog[2][0])
        elif dic[5-c] == jog[3][1]:
            print(jog[3][0])
    elif dic[5-c] == jog[2][1]:
        print(jog[2][0],end='; ')
        if dic[5-c] == jog[0][1]:
            print(jog[0][0])
        elif dic[5-c] == jog[1][1]:
            print(jog[1][0])
        elif dic[5-c] == jog[3][1]:
            print(jog[3][0])
    elif dic[5-c] == jog[3][1]:
        print(jog[3][0],end='; ')
        if dic[5-c] == jog[0][1]:
            print(jog[0][0])
        elif dic[5-c] == jog[1][1]:
            print(jog[1][0])
        elif dic[5-c] == jog[2][1]:
            print(jog[2][0])
    print()