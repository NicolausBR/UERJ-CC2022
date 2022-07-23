totalpares = 0
totalimpares = 0
somapares = 0

n = int(input('Insira a quantia de termos a serem analisados (0 para encerrar o programa): '))
print('-'*45)
while n != int(0):
    for num in range(1,n+1):   
        if (num%2 == 0):
            somapares +=num
            totalpares += 1

        if (num%2 != 0):
            totalimpares +=1
    
    if totalpares > 0:
        print(f'Ao todo, temos um total de {totalpares} números pares')
        print(f'A média da soma dos pares é = {somapares/totalpares}')
        print('-'*45)
    else:
        print('Apenas o valor "1" detectado, logo, não há números pares')
        print('-'*45)
        
    print(f'Ao todo, temos um total de {totalimpares} números ímpares')
    print('-'*45)
    print('')
                
    n = int(input('Insira a qauantia de termos a serem analisados (0 para encerrar o programa): '))
    totalpares = 0
    totalimpares = 0
    somapares = 0
