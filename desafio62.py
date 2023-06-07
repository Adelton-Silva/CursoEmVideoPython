print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
total = 0
termo = primeiro
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo = termo + razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print('progressao finalizada com um total de {} termos mostrado'.format(total))
print('===== FIM =====')