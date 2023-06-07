num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numwro [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))
print('Acabou')