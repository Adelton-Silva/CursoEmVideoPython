cadastro = list()
pessoas = list()
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    pessoas.append(cadastro[:])
    cadastro.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}...',end=' ')
print(f'\nO menor peso foi de {menor}kg Peso de',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}...',end=' ')
