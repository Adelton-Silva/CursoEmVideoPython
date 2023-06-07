c1 = float(input('Digite o comprimento 1 '))
c2 = float(input('Digite o comprimento 2 '))
c3 = float(input('Digite o comprimento 3 '))
if c1 < c2 + c3 and c2 < c3 + c1 and c3 < c2 + c1:
    if c1 == c2 and c2 == c3:
        print('Forma um triangulo EQUILATERO')
    elif c1 == c2 or c2 == c3 or c1 == c3:
        print('Forma um triangulo ISOSCELES')
    else:
        print('Forma um triangulo ESCALENO')
else:
    print('Nao pode formar um triangulo')