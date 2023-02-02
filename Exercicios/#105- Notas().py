def notas(*num):
    """
    :param num: notas
    :return: dicionario
    """
    dic = {}
    media = 0
    for v in num[0]:
        media += v/len(num[0])
    dic['Total'] = len(num[0])
    dic['Maior'] = max(num[0])
    dic['Menor'] = min(num[0])
    dic['Média'] = media
    if sit == 'S':
        if media >= 7:
            dic['Situação'] = 'BOA'
        else:
            dic['Situação'] = 'RUIM'
    print(dic)

listanotas = []
while True:
    nota = float(input('Nota: '))
    esc = str(input('Continuar? ')).strip().upper()[0]
    listanotas.append(nota)
    if esc == 'N':
        break
sit = str(input('Deseja ver a situação? ')).strip().upper()[0]
notas(listanotas)
