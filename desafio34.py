sal = float(input('Qual o seu salario? '))
if sal > 1250:
    novSal = sal + sal*10/100
    print('Voce teve um aumento de 10% o seu novo salario e {:.2f}'.format(novSal))
else:
    novSal = sal + sal*15/100
    print('Voce teve um aumento de 15% o seu novo salario e {:.2f}'.format(novSal))