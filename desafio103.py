def jogador(nome = '', gols = 0):
    if nome == '':
        nome = '<Desconecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#Programa Principal
print('-'*35)
nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de Gols: '))
print(jogador(nome,gols))