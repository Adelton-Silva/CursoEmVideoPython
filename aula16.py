lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')
num = (9,5,1,4,6,7,8,2,3)
num2 = (11, 18, 22, 10)
c = num + num2
#print(lanche[1])
#print(lanche[-2])
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
#for cont in range(0, len(lanche)):
    #print(f' Eu vou comer {lanche[cont]} na posicao {cont}')
for pos, comida in enumerate(lanche):
    print(f' Eu vou comer {comida} na posicao {pos}')
print(sorted(lanche))
print(sorted(num))
print(sorted(num2))
print(sorted(c))
print(c.count(11))
print(c.index(11))
print('Comi pra caramba!')