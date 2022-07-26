n = 4
cont = 0
valor = 1

while cont < n:
    soma = 0
    for x in range(1,valor):

        if valor%x == 0:
            soma +=x

    if soma == valor:
        print(valor)
        cont += 1
        valor += 1

    else:
        valor += 1
