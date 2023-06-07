from random import randint
from time import sleep
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
n = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'-=-=-= {"SORTEANDO"} {n} {"JOGOS"} -=-=-=')
tot = 1
lista = list()
jogos = list()
while tot <= n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-='*5,'< BOA SORTE! >','-='*5)


