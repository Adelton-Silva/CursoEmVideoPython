s = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s = s + num
        count = count + 1
if s > 0:
    print('Voce informou {} numeros pares e a  soma de todos e {}'.format(count,s))
else:
    print('Nao foi introduzido nenhum numero par')
