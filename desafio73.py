equipa = ('Barcelona','Real Madrid','Atletico Madrid', 'Real Sociedad','Villarreal', 'Betis','Osasuna',
         'Ath. Bilbao','Girona','Rayo Vallecano','Sevilla','Mallorca','Cadiz','Getafe','Valencia','Almeria',
         'Celta de Vigo','Real Valladolid','Espanyol','Elche')
print('-='*64)
print('Lista dos times da La Liga:',end=' ')
print(equipa)
print('-='*64)
print('Os 5 primeiros sao :',end=' ')
print(equipa[:5])
print('-='*64)
print('Os 4 ultimos sao:',end=' ')
print(equipa[len(equipa)-4:len(equipa)])
print('-='*64)
print('Times em ordem alfabetica:',end=' ')
print(sorted(equipa))
print('-='*64)
loc = equipa.index('Barcelona')
pos = loc + 1
nome = equipa[loc]
print(f'O {nome} esta na {pos}ª')
print('-='*64)