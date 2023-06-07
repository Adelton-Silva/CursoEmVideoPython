print('Gerador de PA')
print('-='*10)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
primeiro = termo
cont = 1
decimo = termo + (10 -1)*razao
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro = primeiro + razao
    cont += 1
print('FIM')
