def metade(n=0):
    m = n/2
    return m


def dobro(n = 0):
    d = n * 2
    return d


def perc(n = 0, taxa = 0):
    p = n + n*taxa/100
    return p

def moeda(n = 0, moeda = '$00'):
    return f'{n:.2f}{moeda}'.replace('.',',')