n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2 
e = n1**n2
r = n1%n2
print('A soma e {},  o produto e {}, e a divisao e {}'.format(s, m, d), end=' >>> ')
print('Divisao inteira {}, potencia {} e resto da divisa {}'.format(di, e, r))