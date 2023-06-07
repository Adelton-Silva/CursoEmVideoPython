nome = str(input('Qual o seu nome? '))
if nome == 'Adelton':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome e bem popular em Cabo Verde")
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome femenino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia \033[1;31;40m{}\033[m'.format(nome))
