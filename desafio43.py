#idade = int(input('Qual e a sua idade? '))
peso = float(input('Qual e o seu peso(kg)? '))
altura = float(input('Qual e a sua altura(m)? '))
imc = peso/(altura**2)
print('O seu IMC e {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso normal!')
elif imc < 25:
    print('Peso ideal, parabens!')
elif imc < 30:
    print('Sobrepeso ideal!')
elif imc < 40:
    print('Obesidade, cuidado!!')
else:
    print('Obesidade Morbida cuidado!!!!!')

