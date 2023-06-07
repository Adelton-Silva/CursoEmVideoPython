man = 0
maior = 0
woman = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        man += 1
    if sexo == 'F' and idade < 20:
        woman += 1
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {man} homes cadastrados.')
print(f'E temos {woman} mulheres com menos de 20 anos.')

