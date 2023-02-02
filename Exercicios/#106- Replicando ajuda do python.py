def ajuda(msg):
    help(msg)
while True:
    comando = str(input('Comando: ')).strip().lower()
    if comando == 'fim':
        break
    ajuda(comando)
