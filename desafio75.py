num = (int(input('Digite o 1º valor: ')),
        int(input('Digite o 2º valor: ')),
        int(input('Digite o 3º valor: ')),
        int(input('Digite o 4º valor: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if num.count(3) > 0:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posicao')
else:
    print('Nao foi digitado o valor 3')
print(f'Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end='')
    



