def aumentar(n, q, b=True):
    if n < 0 :
        if b:
            return f'R$ {n * (1 - q/100)}'
        else:
            return n * (1 - q/100)
    else:
        if b:
            return f'R$ {n * (1 + q/100)}'
        else:
            return n * (1 + q/100)


def diminuir(n, q, b=True):
    if n < 0 :
        if b:
            return f'R$ {n * (1 + abs(q)/100)}'
        else:
            return n * (1 + abs(q) / 100)
    else:
        if b:
            return f'R$ {n * (1 - abs(q)/100)}'
        else:
            return n * (1 - abs(q) / 100)


def dobro(n=1, b=True):
    if b:
        return f'R$ {n*2}'
    else:
        return n*2


def metade(n=1, b=True):
    if b:
        return f'R$ {n/2}'
    else:
        return n/2


def prefixo(x,b=True):
    if b:
        return f'R$ {x}'
    else:
        return x


def resumo(p=0, a=0, r=0):
    print('_'*45)
    print(f'{"RESUMO DO VALOR": ^45}')
    print('_'*45)
    print(f'{"Preço analisado:":<35}', f'{"R$ "+str(p):<10}')
    print(f'{"Dobro do preço:":<35}', f'{dobro(p):<10}')
    print(f'{"Metade do preço:":<35}', f'{metade(p):<10}')
    print(f'{str(a) + "% de aumento:":<35}', f'{aumentar(p,a):<10}')
    print(f'{str(r) + "% de redução:":<35}', f'{diminuir(p,r):<10}')
    print('_'*45)
