print('Lembre-se, o valor de A não pode ser maior do que o de B!')
print('-'*57)
a = int(input('A = '))
b = int(input('B = '))
print('')
multiplos = 0

while a > b:
    print('O valor de A não pode ser maior que o de B, tente novamente.')
    print('')
    a = int(input('A = '))
    b = int(input('B = '))
    
for num in range (a, b):
    if num%4 == 0:
        multiplos += num

if multiplos <= 0:
    print('Não existe nenhum valor múltiplo de 4 entre A e B, logo não existe soma')

else:
    print(f'A soma dos números múltiplos de 4 entre A e B é = {multiplos}.')
        
    
