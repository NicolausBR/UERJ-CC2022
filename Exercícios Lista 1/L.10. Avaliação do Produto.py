positivo = 0
negativo = 0
total = 0

feedback = str(input('Você gostou do nosso produto? Digite "S" se gostou ou "N" se não gostou: '))
print('-'*50)

while feedback !='f' and feedback !='F':
    if feedback == 'S' or feedback == 's':
        positivo += 1

    elif feedback == 'N' or feedback == 'n':
        negativo += 1

    else:
        print('Erro, tente novamente')
        
    print('')
    feedback = str(input('Você gostou do nosso produto? Digite "S" se gostou ou "N" se não gostou: '))

total = positivo + negativo
pornegativo = float(negativo/total)*100
porpositivo = float(positivo/total)*100
print('-'*50)
print(f'Total de entrevistados = {total} pessoas')
print('-'*50)
print(f'Pessoas que gostaram = {positivo}.')
print(f'{porpositivo:.2f}%')
print('')
print(f'Pessoas que não gostaram = {negativo}.')
print(f'{pornegativo:.2f}%')

               
