print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10 -1)*razao
for c in range(termo, decimo + 1, razao): 
    print(c, end=' -> ')
print('ACABOU')