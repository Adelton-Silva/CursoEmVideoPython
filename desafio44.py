print('{:=^40}'.format(' Lojas SILVA '))
preco = float(input('Qual e o preco do produto '))
print('='*40)
print('1 - A vista com Dinheiro/Cheque')
print('2 - A Vista no cartao')
print('3 - Em ate 2x no cartao')
print('4 - 3x ou mais no cartao')
print('='*40)
op = int(input('Modo de pagamento '))
if op == 1:
    print('Pagamento a vista dinheiro/checque 10% de sesconto')
    preco_final = preco - preco*10/100
    print('Total a pagar e {:.2f}'.format(preco_final))
elif op == 2:
    print('Pagamento a vista no cartao 5% de sesconto')
    preco_final = preco - preco*5/100
    print('Total a pagar e {:.2f}'.format(preco_final))
elif op == 3:
    print('Pagamento em ate 2x no cartao nao tera descontos nem juros')
    parcela = preco/2
    print('Total a pagar e {:.2f} em duas parcelas de {}'.format(preco, parcela))
elif op == 4:
    print('Pagamento em ate 3x no cartao tera um juro de 20%')
    preco_final = preco + preco*20/100
    totparc = int(input('Quantas parcelas? '))
    parcela = preco_final/totparc
    print('Total a pagar e {:.2f} em {} parcelas de {}'.format(preco_final,totparc,parcela))
else:
    print('OPCAO INVALIDA de pagamento. Tente novamente')
