matriz = [[],[],[]]
soma_par = 0
soma_ter = 0
maior = 0
for c in range(0,3):
    for i in range(0,3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
print('-='*30)
for c in range(0,3):
    for i in range(0,3):
        if matriz[c][i] % 2 == 0:
            soma_par += matriz[c][i]
        if i == 2:
            soma_ter += matriz[c][2]
        print(f'[{matriz[c][i]:^5}]',end='')
        if c == 1:
            maior = matriz[1][0]
        else:
            if matriz[1][i] > maior:
                maior = matriz[1][i]
    print()
print('-='*30)
print(f'A soma dos valores pares e {soma_par}.')
print(f'A soma dos valores da terceira coluna e {soma_ter}.')
print(f'O maior valor da segunda linha e {maior}.')
