print('-'*30)
print('   Sequencia de fibonacci')
print('-'*30)
num = int(input('Quantos termos voce quer mostrar: '))
print('~'*30)
cont = 0
n1 = 0
n2 = 1
while cont <= num - 1:
    print('{} -> '.format(n1), end='')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    #print('{}'.format(n3))
print('Fim')
print('~'*30)