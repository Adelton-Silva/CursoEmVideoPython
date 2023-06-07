'''num = [2,5,9,1]
num[2] = 3
num.append(7)
#num.sort()
#num.sort(reverse=True)
#del(num[0])
#num.pop(3)
#num.remove(2)
#num.insert(2,0)
print(num)'''
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')