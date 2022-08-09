lista1 = []
lista2 = []
listaf = []

#VALORES PARA PRIMEIRA LISTA

n = int(input('Valor para a Lista 1 = '))
while n > 0:
    lista1.append(n)
    n = int(input('Valor para a Lista 1 = '))

print('-'*50)

#VALORES PARA SEGUNDA LISTA

n = int(input('Valor para a Lista 2 = '))
while n > 0:
    lista2.append(n)
    n = int(input('Valor para a Lista 2 = '))

#COMPARAÇÃO ENTRE AS LISTAS
    
print('Elementos que aparecem nas duas listas:')
print('')
for i in range (0, len(lista1)):
    for x in range(0, len(lista2)):

        if lista1[i] == lista2[x]:
            
            listaf.append(lista1[i])
            
print(listaf)
print('-'*50)
for i in range (0, len(lista1)):
    cont = lista2.count(lista1[i])
    print(f'O número {lista1[i]} aparece {cont} vez(es).')
            
