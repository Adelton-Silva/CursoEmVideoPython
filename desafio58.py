from random import randint
n = randint(0, 10)
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
while not acertou:
    num = int(input('Qual e o seu palpite? '))
    if n == num:
        acertou = True
    else:
        if n < num:
            print('Menos... Tente mais uma vez.')
        elif n > num:
            print('Mais... Tente mais uma vez.')
    tentativas +=1
print('Acertou com {} tentativas. Parabens!'.format(tentativas))