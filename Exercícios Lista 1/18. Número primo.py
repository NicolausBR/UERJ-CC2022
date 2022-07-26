n = int(input('Número para verificar se é primo = '))

if n > 1:
    for num in range (2, n):
        if (n%num) == 0:
            print(f'O número {n} não é primo')

        else:
            print(f'{n} é um número primo.')

        break


elif n == 1:
    print('1 não é primo.')

elif n == 0:
    print('O número digitado é 0.')

else:
    print('O número é negativo')
