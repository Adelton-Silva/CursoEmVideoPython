from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = False
while not op:
    print('     [1] somar')
    print('     [2] multiplicar')
    print('     [3] maior')
    print('     [4] novos numeros')
    print('     [5] sair do programa')
    opcao = int(input('>>>>> Qual e a sua opcoa? '))
    if opcao == 1:
        s = n1 + n2
        print('A soma entre {} + {} e {}'.format(n1,n2,s))
    elif opcao == 2:
        m = n1 * n2
        print('A multiplicacao entre {} * {} e {}'.format(n1,n2,m))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior e {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior e {}'.format(n1, n2, n2))
        else:
            print('Os valores sao iguais')
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        op = True
    else:
        print('Opcao invalida... Tente novamente!')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')

