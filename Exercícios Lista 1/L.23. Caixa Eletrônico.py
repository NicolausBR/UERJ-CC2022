n50 = n20 = n10 = n5 = n1 = int(0)

print('Cédulas disponíveis nesse caixas: 50, 20, 10, 5, 1.')
print('-'*50)
saque = int(input('Valor a ser sacado em R$ = '))

total = saque

while saque != 0:

    n50 = saque//50
    resto50 = saque%50

    if resto50 != 0:
        n20 = resto50//20
        resto20 = resto50%20

        if resto20 != 0:
            n10 = resto20//10
            resto10 = resto20%10

            if resto10 != 0:
                n5 = resto10//5
                resto5 = resto10%5

                if resto5 != 0:
                    n1 = resto5//1

    print('-'*50)
    print('Foram sacadas:')
    print('')
    print(f'50 = {n50} nota(s)')
    print(f'20 = {n20} nota(s)')
    print(f'10 = {n10} nota(s)')
    print(f'5 = {n5} nota(s)')
    print(f'1 = {n1} nota(s)')
    print('-'*50)

    saque = int(input('Valor a ser sacado em R$ = '))
    
