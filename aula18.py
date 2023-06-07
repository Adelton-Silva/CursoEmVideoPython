teste = list()
teste.append('Adelton')
teste.append(31)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 41
galera.append(teste[:])
print(galera)