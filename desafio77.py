lista = ('Apreder','Programar',
         'Linguagem','Python',
         'Curso','Gratis',
         'Estudar','Praticar',
         'Trabalhar','Mercado',
         'Programador','Futuro')
cont = 0
for p in lista:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
