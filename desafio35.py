print('-='*20)
print('Analisador de triangulo')
print('-='*20)
r1 = int(input('Qual e comprimento da primeira reta? '))
r2 = int(input('Qual e comprimento da segunda reta? '))
r3 = int(input('Qual e comprimento da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas tres retas podem formar um triangulo sim')
else:
    print('Essas tres retas nao formam um triangulo')