import random
n1 = input('Digite o nome do 1 aluno ')
n2 = input('Digite o nome do 2 aluno ')
n3 = input('Digite o nome do 3 aluno ')
n4 = input('Digite o nome do 4 aluno ')
lista = [n1, n2, n3, n4]
esc = random.choice(lista)
print('O aluno escolhido foi {}'.format(esc))
