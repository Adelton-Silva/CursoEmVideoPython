aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
elif aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'- {k} e igual a {v}')
