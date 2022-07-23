total = 0
for produtos in range(1,51):
    valor = float(input('Valor do produto em R$ = '))
    quantidade = int(input('Quantidade do produto = ' ))
    print('-'*30)
    total = total+(valor*quantidade)

print(f'A empresa gastou um total de R$ {total} em produtos nessa compra.')
