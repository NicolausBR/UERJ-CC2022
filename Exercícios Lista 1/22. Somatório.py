soma = 0
n = int(input('Valor de N = '))
print('-'*40)

for i in range (1,n+1):
    somatorio = 1/i
    soma += somatorio
   
print(f'Resultado do somatório = {soma}')
