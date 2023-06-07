v = float(input('Qual a velocidade do carro: '))
if v > 80:
    m = (v - 80)*7
    print('A sua velocidade e de {}km/h, {} acima do limite permitido'.format(v,v-80))
    print('A multa vai ser {:.2f}!'.format(m))
else:
    print('Tenha um bom dia!  Dirija com seguranca')