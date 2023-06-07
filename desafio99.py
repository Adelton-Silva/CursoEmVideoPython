from time import sleep
def maior (*num):
    maior = menor = 0
    print('-='*30)
    print('Analizando os valores passados...')
    for i in range(0,len(num)):
        print(f'{num[i]}',end=' ', flush=True)
        sleep(0.3)
        if i == 0:
            maior = menor = num[i]
        else:
            if num[i] > maior:
                maior = num[i]
            if num[i] < menor:
                menor = num[i]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor passado foi {maior}.')
    print(f'O menor valor passado foi {menor}.')


#Programa Principal
maior(8,5,6,9,1,0)
maior(11,100,10)
maior(10,5,2,9)
maior(6)
maior()