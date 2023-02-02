lista = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',5)
x = 1
print(f'~~'*25 ,f"\n{'PREÇOS':-^50} \n" ,'~~'*25 )
for c in range (0, len(lista),2):
    print(f"{lista[c]:.<43}", end=' ')
    print(f"R${lista[x]:>5,.2f}")
    x += 2
print('~~'*25)