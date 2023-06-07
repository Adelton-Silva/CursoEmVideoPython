import math
ca = float(input('Digite o valor do cateto adjecente '))
co = float(input('Digite o valor do cateto oposto '))
#h = math.pow(ca,2) + math.pow(co,2)
h = math.hypot(co, ca)
print('O valor da hipotinusa e {:.2f}'.format(h))
