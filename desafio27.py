nome = str(input('Qual e o seu nome completo? ')).strip()
sep = nome.split()
print('Seu primeiro nome e {}'.format(sep[0]))
print('Seu ultimo nome e {}'.format(sep[len(sep)-1]))
