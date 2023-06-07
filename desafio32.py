from datetime import date
ano = int(input('Digite um ano qualquer ou coloque 0 para a data atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} e um ano bisexto'.format(ano))
else:
    print('{} nao e um ano bisexto'.format(ano))
