lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'Voce digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 nao foi encontrado na lista!')
