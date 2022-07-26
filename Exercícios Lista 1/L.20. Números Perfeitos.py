n = int(input('Descubra se um número é perfeito: '))
print('-'*50)
soma = 0

for num in range(1,n):
    if (n%num == 0):
        soma += num

if soma == n:
    print(f'O número {n} é um número perfeito pois a soma de seus divisores é igual ao valor inserido!')

else:
    print(f'O número {n} não é um número perfeito')
