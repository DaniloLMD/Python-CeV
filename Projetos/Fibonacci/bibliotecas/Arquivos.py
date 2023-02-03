def criarArquivo(nome):
    """
    A função tentará abrir um arquivo, se não conseguir ela criará um arquivo com o mesmo nome.
    """
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
        print(f'Arquivo "{nome}" já existe!')
    except:
        arquivo = open(nome, 'wt+')
        arquivo.close()
        print(f'Arquivo "{nome}" criado com sucesso!')

def EscreverDic(x, nomeArquivo):
    dic = x
    if type(dic) != dict:
        print(f'{dic} não é um dicionário!')
    else:
        criarArquivo(nomeArquivo)
        arquivo = open(nomeArquivo, 'at')
        print('Dados transcritos com sucesso!')
        arquivo.write(title('Fibonacci por Pyr'))
        for keys, values in dic.items():
            arquivo.write(f'{keys:<10}: {values}\n')
        arquivo.close()

def leiaInt(msg):
    while True:
        num = input(msg)
        try:
            return int(num)
        except:
            print(f'O valor {num} não é inteiro!')


def title(msg):
    tamanho = 100
    return f'{"~"*tamanho}\n{msg.center(tamanho)}\n{"~"*tamanho}\n'


def Fibonacci(x):
    if x > 0:
        termosLista = [1 , 1]
        for c in range(3, x + 1):
            termosLista.append(termosLista[c-2] + termosLista[c-3])
        termos = {}
        for c in range(1, x + 1):
            termos[f'Termo {c}'] = termosLista[c-1]
        EscreverDic(termos, f'Fibonacci {x} termos')