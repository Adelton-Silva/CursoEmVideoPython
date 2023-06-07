from random import randint
from time import sleep
def gerador(lst):
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        lst.append(randint(0,10))
        print(lst[i], end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def soma(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valors pares de {lst}, temos {soma}')



#Programa Principal
lst = list()
gerador(lst)
soma(lst)

