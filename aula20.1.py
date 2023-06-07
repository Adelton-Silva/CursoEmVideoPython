'''def soma(a,b):
    print(f'A = {a} e B = {b} ')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


#Programa Principal
soma(b = 4, a = 5)
soma(8,9)
soma(2,1)'''
'''def contador(*num):
    tan = len(num)
    print(f'Reebi os valores {num} e sao ao todo {tan} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 1, 7, 8, 9)'''

'''def dobra(lst):
    c = 0
    while c < len(lst):
        lst[c] *= 2
        c +=1


valores = [6, 4, 8, 5, 7, 9]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)