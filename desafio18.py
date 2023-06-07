import math
n = float(input('Digite um grau: '))
cos = math.cos(math.radians(n))
sen = math.sin(math.radians(n))
tan = math.tan(math.radians(n))
print('O seno de {} e {:.2f} \n cos e {:.2f} \n  tan e {:.2f}'.format(n, sen, cos, tan))
