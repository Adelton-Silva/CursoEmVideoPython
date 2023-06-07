cadastrar = dict()
lista = list()
soma = 0
while True:
    cadastrar['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: ')).strip().upper()
    if sexo not in 'MF':
        while sexo not in 'MF':
             print('ERRO! Pesponda M ou F.')
             sexo = str(input('Sexo: ')).strip().upper()
    cadastrar['sexo'] = sexo
    cadastrar['idade'] = int(input('Idade: '))
    soma += cadastrar['idade'] 
    lista.append(cadastrar.copy())
    r = str(input('Quer Continuar? [S/N] ')).strip().upper()
    if r not in 'SN':
        while r not in "NS":
            print('ERRO! Pesponda S ou N.')
            r = str(input('Quer Continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-='*30)
media = soma/len(lista)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A media de idade e de {media:.2f}')
print('As mulheres cadastradas foram',end=' ')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'],end=' ')
print()
print('Lista das pessoas que estao acima da media')
for c in lista:
    if c['idade'] >= media:
        print('    ',end='')
        for k, v in c.items():
            print(f'{k} = {v}', end=', ')
        print()
print('<<< ENCERRADO >>>')