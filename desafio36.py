casa = float(input('Qual e o valor da casa? '))
sal = float(input('Qual o seu salario? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
minimo = sal*30/100
print('Para pagar uma casa de {:.2f}ECV em {} anos'.format(casa, anos), end='')
print('a prestacao sera de {:.2f}ECV'.format(prestacao))
if prestacao <= minimo:
    print('\033[1;32mEmprestimo pode ser CONCEDIO!\033[m')
else:
    print('\033[1;31mEmprestimo pode ser NEGADO!\033[m')
