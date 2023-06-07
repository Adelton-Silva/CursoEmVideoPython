import random
from time import sleep
print('\033[1;34m-=-\033[m' * 20)
print('\033[1;33mVou pensar em um numero entre a e 5. Tente adivinhar\033[m')
print('\033[1;34m-=-\033[m' * 20)
n = random.randint(0,5)
num = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('\033[32mParabens voce acertou!\033[m')
else:
    print('\033[1;31;40mErrou feio em amigo\033[m')
    print('Voce digitou \033[35m{}\033[m e o computador pensou \033[36m{}\033[m'.format(num, n))