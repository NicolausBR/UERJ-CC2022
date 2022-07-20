produto = str
produtocaro = str
produtocarov = 0

while produto != 'XXX' or produto != 'xxx':
    print('-'*40)
    produto = input('Nome do Produto:')
    if produto == 'XXX' or produto == 'xxx':
        break
    
    vproduto = float(input('Valor do Produto em R$:'))

    if vproduto > produtocarov:
        produtocaro = produto
        produtocarov = vproduto


print('Produto mais caro:',produtocaro,', com valor de R$',produtocarov)
    
    


