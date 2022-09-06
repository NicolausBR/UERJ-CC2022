vetor = []
encontros = 0

print('Primeiro vamos colocar os valores no vetor para fazer a anaĺise.')
print('OBS: Se um número não inteiro for digitado somente sua parte inteira será contada.')
print('')

for i in range(0,30):
    valor = int(input(f'{i+1}º Valor: '))
    vetor.append(valor)

print('')
busca = int(input('Agora insira o valor para ser encontrado na lista: '))
print('-'*70)

for x in range(0,len(vetor)):
    if vetor[x] == busca:
        encontros +=1

if encontros == 0:
    print('Esse valor não está presente no vetor.')

else:
    print(f'O número {busca} foi encontrado {encontros} vezes no vetor')
