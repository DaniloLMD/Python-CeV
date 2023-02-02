def vota(a):
    if 16 <= a < 18 or a >= 65:
        return 'OPCIONAL'
    elif a < 16:
        return 'NEGADO'
    elif 18 <= a < 65:
        return 'OBRIGATÓRIO'

from datetime import date
idade = date.today().year - int(input('Ano de nascimento: '))
print(f'com {idade:^5}anos : VOTO {vota(idade):^10}')
