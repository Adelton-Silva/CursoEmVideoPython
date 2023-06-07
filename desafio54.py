from datetime import date
ano_act =date.today().year
cont_mai = 0
cont_men = 0
for c in range(1, 8):
    ano_nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = ano_act - ano_nasc
    if idade >= 18:
        cont_mai +=1
    else:
        cont_men +=1
print('No total temos {} maiores de idade e {} menores de idade'.format(cont_mai, cont_men))
