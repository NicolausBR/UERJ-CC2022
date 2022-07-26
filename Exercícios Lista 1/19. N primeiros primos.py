divisores = 0
qprimos = 0

n = int(input('Primeiros primos a serem encontrados = '))
v = 2

while qprimos < n:
    for i in range(1,v+1):
        if v%i == 0:
            divisores += 1

    if divisores == 2:
        qprimos += 1
        print(f'{v} é primo')
            

    v +=1
    divisores = 0
