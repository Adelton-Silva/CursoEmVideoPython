import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError:
    print('O site Pudim nao esta acessivel no momento.')
else:
    print('Consegui acessar o site Google com sucesso!')
    