#Programa para calcular a soma de todos os números entre dois n inteiros, onde A < B.

soma = 0

print('A seguir, insira um valor para "A" e para "B" para fazer a soma dos números entre eles, onde A < B.')

a = int(input('A = '))
b = int(input('B = '))
print('-'*40)


while a > b:
    print('O valor de A não pode ser maior do que o de B, tente novamente')
    print('-'*40)
    a = int(input('A = '))
    b = int(input('B = '))
    
    
for numeros in range (a,b+1):
    soma +=numeros
    print (numeros)

print(f'A soma dos números entre A e B são no total: {soma}.')
    
