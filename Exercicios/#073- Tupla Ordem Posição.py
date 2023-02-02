classes = ['Osamodas','Sacrier','Pandawa','Ladino','Feca','Sadida','Enutrof','Xelor','Eniripsa','Zobal'
    ,'Iop', 'Sram','Cra','Ecaflip','Kilorf','Hupper','Elio','Steamer']
c = 0
print(f'Os 4 ultimos colocados da tabela foram: ', end='')
for c in range (14,18) :
    print(classes[c], end = ' , ') if c < 17 else print(classes[c]+ ' .')
print('~~'*25)
print(f'Os 5 primeiros colocados foram: ', end = '')
for c in range (0, 6):
    print(classes[c], end = ' , ') if c < 5 else print (classes[c]+'.')
print('~~'*25)
print(f'Em ordem alfabetica: ',end = '')
for c in range (0,18):
    print(sorted(classes)[c], end = ' , ') if c < 17 else print(sorted(classes)[c]+'.\n')
classe = str(input('Qual classe você quer saber? '))
print(f'A classe {classe} está na posição {classes.index(classe)}')