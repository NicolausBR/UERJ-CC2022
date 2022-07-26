c1 = 0
c2 = 0
c3 = 0
c4 = 0
branco = 0
nulo = 0

print('Possíveis Votos:')
print('1 - João da Silva')
print('2 - José Ramalho')
print('3 - Maria Mattos')
print('4 - Pedro Américo')
print('0 - Voto em Branco')
print('Qualquer outro valor - Voto Nulo')
print('-'*50)

for votos in range(1, 20001):

    voto = int(input(f'Dígito do {votos}º voto = '))
    print('')

    if voto == 1:
        c1 += 1

    elif voto == 2:
        c2 +=1

    elif voto == 3:
        c3 += 1

    elif voto == 4:
        c4 += 1

    elif voto == 0:
        branco += 1

    else:
        nulo +=1

print(f'João da Silva = {c1} votos')
print('')
print(f'José Ramalho = {c2} votos')
print('')
print(f'Maria Mattos = {c3} votos')
print('')
print(f'Pedro Américo = {c4} votos')
print('')
print('-'*50)
print(f'Votos em Branco = {branco} votos')
print(f'Votos Nulos = {nulo} votos')
print('-'*50)
