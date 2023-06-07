def metade(n=0, formato = False):
    m = n/2
    return m if formato is False else moeda(n)


def dobro(n = 0, formato = False):
    d = n * 2
    return d if formato is False else moeda(n)


def perc(n = 0, taxa = 0, formato = False):
    p = n + n*taxa/100
    return p if formato is False else moeda(n)


def red_perc(n = 0, taxa = 0, formato = False):
    p = n - n*taxa/100
    return p if formato is False else moeda(n)


def moeda(n = 0, moeda = '$00'):
    return f'{n:.2f}{moeda}'.replace('.',',')

