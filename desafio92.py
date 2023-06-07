from datetime import datetime
pessoas = dict()
while True:
    pessoas['nome'] = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    pessoas['idade'] = datetime.now().year - ano_nascimento
    pessoas['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
    if pessoas['ctps'] == 0:
        break
    pessoas['contratacao'] = int(input('Ano de Contratacao: '))
    pessoas['salario'] = float(input('Salario: '))
    pessoas['aposentadoria'] = pessoas['idade'] + ((35 + pessoas['contratacao']) - datetime.now().year)
    break
print('-='*30)
for k, v in pessoas.items():
    print(f' - {k} tem o valor {v}')