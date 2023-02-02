from utilidades import dado, moeda
valor = dado.leiadin('Valor: R$')
aum = float(input('Aumento(em %): '))
dim = float(input('Redução(em %): '))
moeda.resumo(valor, aum, dim)