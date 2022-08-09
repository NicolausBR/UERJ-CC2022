listanomes = []
listanotas = []
maioresnotas = []
maiornota = -1
imaiornota = 0

print('O programa será encerrado  irá imprimir os dados quando o nome inserido for "x"')
print('')
nome = str(input('Nome do Aluno: '))

while nome != 'X' and nome != 'x':
    nota = float(input('Nota do Aluno: '))
    print('-'*50)
    listanomes.append(nome)
    listanotas.append(nota)

    nome = str(input('Nome do Aluno: '))

for i in range (0, len(listanotas)):
    if listanotas[i] > maiornota:
        imaiornota = i
        maiornota = listanotas[i]
        maioresnotas = []
        maioresnotas.append(i)

    elif listanotas[i] == maiornota:
        maioresnotas.append(i)

print('-'*50)
print(f'Alunos com a maior nota: (maior nota = {maiornota})')
print('')

for i in range (0, len(maioresnotas)):

    print(f'{listanomes[maioresnotas[i]]} tem a maior nota')
    print('')

    
