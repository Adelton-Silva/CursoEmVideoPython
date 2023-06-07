valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
print('=-'*30)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e foi nas posicoes',end=' ')
for pos, n in enumerate(valores):
    if valores[pos] == max(valores):
        print(f'{pos}...',end=' ')
print(f'\nO nemor valor digitado foi {min(valores)} e foi nas posicoes',end=' ')
for pos, n in enumerate(valores):
    if valores[pos] == min(valores):
        print(f'{pos}...',end=' ')

'''Alternativa para maior e menor declarar maior e menor como 0 no inicio
e logo apos o for para entrada de dados fazer:
if c == 0:
    maior = menor = valores[c]
else:
    'if valores[c] > maior
        maior = valores[c]
     if valores[c] < menor
        mnemor = valores[c]'''