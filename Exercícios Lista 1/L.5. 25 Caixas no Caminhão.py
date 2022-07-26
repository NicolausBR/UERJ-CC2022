pesot = 0

print('A seguir, insira o peso de cada uma das 25 caixas em KG:')
print('')

for peso in range (1,26):
    float(input(f'Peso na caixa {peso}:'))
    print('')

    pesot += peso

print('O peso total do caminhão será:',pesot,'Kg')
