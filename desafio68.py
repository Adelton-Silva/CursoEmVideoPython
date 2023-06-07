from random import randint
vitoria = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    computador = randint(0, 10)
    jogador= int(input('Digite um valor: '))
    palpite = ' '
    while palpite not in 'PI':
        palpite = str(input('Par ou Impar? [P/I] ')).strip().upper()
    resultado = computador + jogador
    if resultado % 2 == 0:
        prim = 'PAR'
    else:
        prim = 'IMPAR'
    print('-'*30)
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {resultado} DEU {prim}')
    print('-'*30)
    if resultado % 2 == 0 and palpite == 'P':
        print('Voce VENCEU!')
        print('Vamomos jogar novamente...')
        vitoria += 1
        print('=-'*15)
    elif resultado % 2 != 0 and palpite == 'I':
        print('Voce VENCEU!')
        print('Vamomos jogar novamente...')
        vitoria +=1
        print('=-'*15)
    else:
        break
print('Voce PERDEU!')
print('=-'*15)
print(f'Game OVER! Voce venceu {vitoria} vezes.')

