lista = []
listafinal = []

# Coloquei XX pra encerrar pois a pessoa pode querer inserir um x na lista.

n = str(input('Insira um(a) número/letra ou "XX" para finalizar: '))


while n != 'XX' and n != 'xx' and n!='Xx' and n !='xX':

    lista.append(n)
    listafinal.append(n)
    
    print('')
    n = str(input('Insira um(a) número/letra ou "XX" para finalizar: '))
    

for i in range(0,len(listafinal)-1):
    for j in range (i+1, len(listafinal)):
        if listafinal[i] > listafinal[j]:
            valor = listafinal[i]
            listafinal[i] = listafinal[j]
            listafinal[j] = valor
print('')
print(f'Primeira Lista: {lista}') 
print(f'Lista ordenada: {listafinal}')
print('-'*100)
print('Tenha um bom dia :D')

