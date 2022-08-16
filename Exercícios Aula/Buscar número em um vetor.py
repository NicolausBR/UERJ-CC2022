vetnum = []
pos = []

num = int(input('Número pra adicionar a lista (Insira n < 0 para encerrar) = '))
while num >= 0:
    vetnum.append(num)
    print('')
    num = int(input('Número pra adicionar a lista (Insira n < 0 para encerrar) = '))
print('-'*100)
valor = int(input('Insira o número a ser buscado na lista: '))

for i in range (0, len(vetnum)):
    if valor == vetnum[i]:
        pos.append(i)

if len(pos) == 0:
    print('Erro, esse número não está presente na lista inserida anteriormente')

else:
    print(f'O número {valor} foi encontrado na(s) posição(ões) {pos}, dando um total de {len(pos)} vezes')
    
