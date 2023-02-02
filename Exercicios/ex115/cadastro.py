def l():
    print('-' * 50)


def cadastro():
    nomes = []
    idades = []
    cadastro = {}
    while True:
        l()
        print('MENU PRINCIPAL'.center(50))
        l()
        print('1- Ver pessoas cadastradas')
        print('2- Cadastrar nova pessoa')
        print('3- Sair do sistema')
        l()
        op = input('Sua opção: ').strip()
        if len(op) != 1 or op not in '123':
            print('Opção inválida!')
            l()
        if op == '1':
            l()
            print('CADASTROS'.center(50))
            l()
            for c in range(0, len(nomes)):
                print(f'{nomes[c]:<40} {idades[c]:>9}')
        elif op == '2':
            l()
            print('NOVO CADASTRO'.center(50))
            l()
            while True:
                novonome = input('Nome: ')
                novaidade = input('Idade: ')
                if novaidade.isnumeric():
                    nomes.append(novonome)
                    idades.append(novaidade)
                    break
                else:
                    print('Idade inválida!')
        elif op == '3':
            l()
            cadastro['Nomes'] = nomes[:]
            cadastro['Idades'] = idades[:]
            return cadastro


def organizardic(dicionario):
    l()
    print(f'{"Nomes":<40}{"Idades":>9}\n')
    for c in range(0, len(dicionario["Nomes"])):
        print(f'{dicionario["Nomes"][c]:<40}{dicionario["Idades"][c]:>9}')
    l()
