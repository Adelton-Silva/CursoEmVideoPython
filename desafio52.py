count = 0
num = int(input('Digite um numero: '))
for c in range(1, num+1):
    if num % c == 0:
        count = count + 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c) , end=' ')
if count < 3:
    print('\n{} e Numero primo'.format(num))
else:
    print('\n{} nao e Numero primo'.format(num))