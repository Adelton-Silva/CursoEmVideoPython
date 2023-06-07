from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificacao: MIRIM')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')