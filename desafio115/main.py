from modulos import *
from time import sleep
from arquivos import *
arq  = 'cursoemvideo.txt'

if not arquivivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resp == 1:
        # Opcao de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Opcao de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao valida\033[m')
    sleep(2)