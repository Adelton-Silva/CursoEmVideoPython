def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um mumero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-'*42

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c:>5}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opcao: \033[m')
    return opc
