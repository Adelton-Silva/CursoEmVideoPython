'''c = 1
while c < 11:
    print(c, end=' ')
    c = c + 1
print('FIM')'''
'''n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

cpar = 0
cimpar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            cpar +=1
        else:
            cimpar +=1
print('Foi digitado {} par e {} impar'.format(cpar,cimpar))
