def metade(n=0, formato = False):
    m = n/2
    return m if formato is False else moeda(m)


def dobro(n = 0, formato = False):
    d = n * 2
    return d if formato is False else moeda(d)


def perc(n = 0, taxa = 0, formato = False):
    p = n + n*taxa/100
    return p if formato is False else moeda(p)


def red_perc(n = 0, taxa = 0, formato = False):
    p = n - n*taxa/100
    return p if formato is False else moeda(p)


def moeda(n = 0, moeda = '$00'):
    return f'{n:.2f}{moeda}'.replace('.',',')


def resumo(n = 0, taxa = 10, taxar = 5):
    print('-'*38)
    print('RESUMO DO VALOR'.center(30))
    print('-'*38)
    print(f'Preco analizado: \t{moeda(n)}')
    print(f'Dobro do preco: \t{dobro(n, True)}')
    print(f'Metade do preco: \t{metade(n, True)}')
    print(f'{taxa}% de aumento: \t{perc(n, taxa, True)}')
    print(f'{taxar}% de reducao: \t{red_perc(n, taxar, True)}')
    print('-'*38)