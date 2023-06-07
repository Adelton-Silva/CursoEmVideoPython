from datetime import date
ano_atual = date.today().year
ano = int(input('Ano de de nascimento: '))
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))
if idade == 18:
    print('Voce tem que alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano_ali = ano_atual + saldo
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento sera em {}'.format(ano_ali))
elif idade > 18:
    saldo = idade - 18
    ano_ali = ano_atual - saldo
    print('Voce ja deveria ter alistado ha {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano_ali))