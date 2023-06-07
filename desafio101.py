def calcular_idade(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade}: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: VOTO OPCIONAL'
    else:
        return f'Com {idade}: VOTO OBRIGATORIO'


#Programa principal
print('-'*30)
ano_nasci = int(input('Em que ano voce nasceu? '))
print(calcular_idade(ano_nasci))


