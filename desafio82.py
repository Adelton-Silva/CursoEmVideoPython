lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
par.sort()
impar.sort()
print('-='*30)
print(f'A lista completa e {lista}')
print(f'A lista de pares e {par}')
print(f'A lista de impares e {impar}')