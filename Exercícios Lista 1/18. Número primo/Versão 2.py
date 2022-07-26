qprimos = 0
n = int(input('Número para verificar se é primo = '))

if n > 1:
    for num in range (1, n+1):
        if (n%num) == 0:
            qprimos += 1

    if qprimos == 2:
            print(f'O número {n} é primo')

    else:
            print(f'O número {n} não é primo')
            


elif n == 1:
    print('1 não é primo.')

elif n == 0:
    print('O número digitado é 0.')

else:
    print('O número é negativo')
