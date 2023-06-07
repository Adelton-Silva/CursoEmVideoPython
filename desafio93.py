jogador = dict()
lista = []
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    golos = int(input(f'Quantos gols na partida {c}? '))
    lista.append(golos)
    total += golos
jogador['gols'] = lista[:]
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i,c in enumerate(lista):
    print(f'    => Na partida {i}, fez {c} gols.')
print(f'Foi um total de {total} gols.')