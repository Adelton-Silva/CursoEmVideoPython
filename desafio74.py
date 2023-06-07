from random import randint
ls =(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sortiados sao ', end='')
for n in ls:
    print(f'{n}', end=' ')
print()
print(f'O maior valor sorteado foi {max(ls)} ')
print(f'O menor valor sorteado foi {min(ls)} ')






