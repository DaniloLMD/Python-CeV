def aumentar(n, q):
    return n * (1 + q/100)


def diminuir(n, q):
    if q > 0:
        return n * (1 - q/100)
    else:
        return n * (1 + q/100)


def dobro(n):
    return n*2


def metade(n):
    return n/2

def moeda(n):
    return 'R$' + str(n)
