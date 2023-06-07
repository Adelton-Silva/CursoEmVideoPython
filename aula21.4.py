def factorial(num = 1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont 
    return f
    

#Programa principal
n = int(input('Digite um numero: '))
f = factorial(n)
print(f'O facorial de {n}  e {f}')