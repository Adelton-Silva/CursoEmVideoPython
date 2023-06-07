pessoas = {'nome':'Adelton', 'sexo':'M', 'idade': 22}
'''print(pessoas)
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
