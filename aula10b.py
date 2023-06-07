n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 +n2)/2
print('A sua media foi {:.2f}'.format(m))
if m >= 6.00:
    print('Sua media foi boa! PARRABES')
else:
    print('Sua media foi ruim! ESTUDE MAIS')