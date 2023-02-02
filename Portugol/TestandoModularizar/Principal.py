from bibliotecas.arquivotexto import *
arquivo = 'cadastro.txt'

if arquivoexiste(arquivo):
    print('Arquivo encontrado!')
else:
    print('Arquivo NÃO encontrado!')
    criarArquivo(arquivo)

lerArquivo(arquivo)
escreverArquivo(arquivo, 'Geraldo Daffara', 100)
lerArquivo(arquivo)
