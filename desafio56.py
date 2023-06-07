sIdade = 0
velho = 0
nomeV = ''
woman = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    sIdade += idade
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nomeV = nome
    if sexo == 'F' and idade < 20:
        woman +=1
media = sIdade/4
print('A media de idade do grupo e de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nomeV))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(woman))

