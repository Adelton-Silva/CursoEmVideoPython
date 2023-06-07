r = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while r == 'S':
    num = int(input('Digite um numero: '))
    if cont == 0:
        maior = num
        menor = num
    cont += 1
    soma += num
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma/cont
print('Voce digitou {} numeros e a media foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou')


