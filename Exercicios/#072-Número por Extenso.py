num = ('Zero' , 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis','Sete','Oito','Nove','Dez','Onze'
       ,'Doze','Treze','Quatorze ou Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    esc = int(input('Digite um número de 0 a 20: '))
    if 0 <= esc <= 20 :
        print(f'Você escreveu: {num[esc]}')
        print('~~'*25)
    else :
        print('Opção Inválida!')
        break