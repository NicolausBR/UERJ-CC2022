soma=0
n = int(input('Quantidade de Termos ÍMPARES para serem somados = '))

for num in range (1,n+n,2):
    soma +=num

print('')
print(f'A soma dos {n} primeiros números ímpares é = {soma}')
