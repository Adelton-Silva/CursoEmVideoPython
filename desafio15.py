d = int(input('Quantos dias alugou o carro: '))
km = float(input('Quantos quilometros foi rodado: '))
p = 60*d + 0.15*km
print('O preco total a pagar e de {:.2f}'.format(p))
