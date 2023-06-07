import uteis


num = float(input('Digite o preco: '))
print(f'A metade de {uteis.moeda(num)} e {uteis.metade(num, True)}')
print(f'O dobro de {uteis.moeda(num)} e {uteis.dobro(num, True)}')
print(f'Aumentando 10%, temos {uteis.perc(num, 10, True)}')
print(f'Reduzindo 13%, temos {uteis.red_perc(num, 13, True)}')
