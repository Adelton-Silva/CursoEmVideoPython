frase = input('Digite o seu nome completo ').strip()
print('Analizando seu nome')
print('Seu nome em maiusculas e {}'.format(frase.upper()))
print('Seu nome em minusculas e {} '.format(frase.lower()))
print('Seu nome tem {} letras '.format(len(frase) - frase.count(' ')))
#print('Seu primeiro nome tem {} '.format(frase.find(' ')))
separa = frase.split()
print('Seu primeiro nome e {} e tem {} letras'.format(separa[0], len(separa[0])))



