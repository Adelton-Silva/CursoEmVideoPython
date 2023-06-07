dis = float(input('Quantos quilometros voce vai viajar? '))
print('Voce esta preste a comecar uma viagem de {}km. '.format(dis))
if dis <= 200:
    p = dis * 0.5
    print('O custo da sua viagem sera {:.2f}'.format(p))
else:
    p = dis * 0.45
    print('O custo da sua viagem sera {:.2f}'.format(p))