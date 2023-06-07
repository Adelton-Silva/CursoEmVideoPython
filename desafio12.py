p = float(input('Qual o preco do produto: '))
des = p - (p*5)/100
print('O produto que custava {:.2f} agora com 5% de descontos custa {:.2f}'.format(p, des))