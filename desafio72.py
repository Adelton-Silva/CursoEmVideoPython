num = -1
nome_num = ('Zero','Um','Dois','Tres','Quatro','Cinco',
                'Seis','Sete','Oito','Nove','Dez',
                'Onze','Douze','Treze','Catorze','Quinze',
                'Dezaseis', 'Dezasete', 'Dezoito', 'Dezenove','Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!')
print(f'Voce digitou o numero {nome_num[num]}')
