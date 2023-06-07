num = int(input('Digite um numero para ver sua tabuada Tabuada: '))
print('== Tabuada de {} =='.format(num))
for c in range(1, 11):
    m = c * num
    print('{} * {} = {}'.format(c,num,m))
