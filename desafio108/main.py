import uteis


num = float(input('Digite o preco: '))
print(f'A metade de {uteis.moeda(num)} e {uteis.moeda(uteis.metade(num))}')
print(f'O dobro de {uteis.moeda(num)} e {uteis.moeda(uteis.dobro(num))}')
print(f'Aumentando 10%, temos {uteis.moeda(uteis.perc(num, 10))}')