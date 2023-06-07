try:
    a = int(input('Numerador: '))
    b = int(input('Denumerador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problem com o tipo de dados que voce digitou.')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')