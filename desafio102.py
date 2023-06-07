def fatorial(n, show = False):
    """
    -> Calcula o Fatorial de um munero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta
    :return: O valor do Fatorial de um numero n
    """
    if show == True:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return f'{f}'
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f'{f}'


#Programa Principal
#help(fatorial)
a = int(input('Digite um valor: '))
n = int(input('Quer mostrar com calculo (1 para Sim e 0 para Nao) '))
if n == 1:
    show = True
else:
    show = False
print(fatorial(a, show))
