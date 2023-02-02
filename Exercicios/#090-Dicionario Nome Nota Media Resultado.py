dicionario = {'nome': str(input('Nome: ')),'média': float(input('Média: ')), 'situação': 'em espera'}
if dicionario['média'] >= 7:
    dicionario['situação'] = 'Aprovado'
else:
    dicionario['situação'] = 'Reprovado'
print(f'Nome: {dicionario["nome"]}\nMédia: {dicionario["média"]}\nSituação: {dicionario["situação"]}')
