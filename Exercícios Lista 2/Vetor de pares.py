vetor = []
pares = []
for i in range (0,4):
    valor = int(input(f'Insira o {i+1}º valor: '))
    vetor.append(valor)

for x in range(0,len(vetor)):
    if vetor[x]%2 == 0:
        pares.append(vetor[x])


print('')
print(f'Vetor original (Ordenado): {sorted(vetor)}')

if len(pares) == 0:
    print(f'O primeiro vetor não possui números pares')
else:
    print(f'Vetor apenas com pares (Ordenado): {sorted(pares)}')
