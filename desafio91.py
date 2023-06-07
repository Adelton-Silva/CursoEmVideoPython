from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
jogo = {' Jogador 1': randint(1,6),
        ' Jogador 2': randint(1,6),
        ' Jogador 3': randint(1,6),
        ' Jogador 4': randint(1,6)}
rankig = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-='*30)
print('  ==  RANKING DOS JOGADORES  ==')
rankig = sorted(jogo.items(), key = itemgetter(1), reverse=True)
for k, v in enumerate(rankig):
    print(f'   {k+1}º lugar {v[0]} com {v[1]}')
    sleep(1)