n1 = float(input('Primeira nota '))
n2 = float(input('Segunda nota '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f} a media do aluno e {:.1f}'.format(n1,n2,media))
if media < 5:
    print('O aluno esta REPROVADO!')
elif media >= 5 and media < 7:
    print('O aluno esta em recuperacao RECUPERACAO!')
else:
    print('O aluno esta Aprovado!')
