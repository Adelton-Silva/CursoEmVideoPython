def area(l, c):
    a = l * c 
    print(f'A area de um tereno {l}x{c} e de {a}m2.')


#Programa Principal
print(' Contotrolo de Terrenos')
print('-'*25)
l = float(input('    LARGURA (m): '))
c = float(input('    COMPRIMENTO (m): '))
area(l, c)