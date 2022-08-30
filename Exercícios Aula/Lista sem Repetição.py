def vetcerto(x):
    listaex = []
    for i in range(0, len(x)):
        encontrou = False
        for j in range(0, len(listaex)):
            if x[i] == listaex[j]:
                encontrou = True
        if(not encontrou):
            listaex.append(x[i])
                       
    return listaex


lista = []
valor = str(input('Insira um valor para a lista, ou insira "X" para encerrar: ')).upper()

while valor != 'X':
    
    lista.append(int(valor))
    
    valor = str(input('Insira um valor para a lista, ou insira "X" para encerrar: ')).upper()

novalista = vetcerto(lista)
print(f'Lista inserida: {lista}')
print(f'Lista sem Repetições (Ordenada): {sorted(novalista)}')
