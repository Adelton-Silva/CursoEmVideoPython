n = int(input('Quer ver a tabuada de qual valor? '))
while True:
    c = 1
    print('-'*30)
    while True:
        t = n * c
        c += 1
        print(f'{n} x {c} = {t}')
        if c == 11:
            break
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
