import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print('Consegui acessar o site Pudim!')
except:
    print('O site pudim não está acessível no momento!')
