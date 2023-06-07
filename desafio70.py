print('-'*40)
print('          LOJA SUPER BARATAO')
print('-'*40)
pagar = 0
mais = 0
menor = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: '))
    if menor == 0:
        menor = preco
        barato = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    pagar += preco
    if preco > 1000:
        mais += 1
    if preco < menor:
        menor = preco
        barato = produto
    if r == 'N':
        break
print(f'O total da compra foi {pagar:.2f}')
print(f'Temos {mais} produtos custando mais de 1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')

