jogador = dict()
golos = list()
lista = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome de jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    golos.clear()
    for c in range(1, partidas+1):
        golos.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = golos[:]
    jogador['total'] = sum(golos)
    lista.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(lista):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40) 
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'       No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')

