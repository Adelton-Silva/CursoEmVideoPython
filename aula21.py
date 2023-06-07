'''print(input.__doc__)
help(input)'''
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funcao criada por Adelton Silva durante o curso de Python mundo 3 do curso em video 
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')


help(contador)
contador(2,10,2)
