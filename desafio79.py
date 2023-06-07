valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com Sucesso!')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
valores.sort()
print('-='*30)
print(f'Voce digitou os {valores}')