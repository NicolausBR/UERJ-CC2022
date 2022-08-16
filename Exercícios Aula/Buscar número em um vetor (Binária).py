vetnum = []
pos = []

num = int(input('Número pra adicionar a lista (Insira n < 0 para encerrar) = '))
while num >= 0:
    vetnum.append(num)
    print('')
    num = int(input('Número pra adicionar a lista (Insira n < 0 para encerrar) = '))

vetnum.sort()
print('-'*100)

valor = int(input('Insira o número a ser buscado na lista: '))

inicio = 0
fim = len(vetnum) -1
encontro = False

while inicio <= fim and (encontro == False):
    meio = (inicio + fim)//2
    if valor == vetnum[meio]:
        pos = meio
        encontro = True

    elif valor < vetnum[meio]:
        fim = meio - 1

    else:
        inicio = meio + 1
print('-'*100)

if encontro == False:
    print('O número digitado não está presente na lista.')
    print(f'Lista Ordenada: {vetnum}.')

else:
    print(f'O número {valor} está presente na posição de índice {pos}.')
    print(f'Lista Ordenada: {vetnum}.')
