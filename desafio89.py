temp = list()
alunos = list()
media = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    alunos.append([nome,[n1, n2], media])
    temp.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-='*40)
print('{:<4}{:<10}{:>8}'.format('Nº','NOME','MEDIA'))
print('-'*50)
for pos, v in enumerate(alunos):
    print(f'{pos:<4}{v[0]:<10} {v[2]:>8}')   
print('-'*50)
while True:
    opc = int(input('Mostre notas de qual de aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} sao {alunos[opc][1]}')
        print('-'*50)
print('<<< VOLTE SEMPPRE >>>')
