soma = 0
cont = 0
notas = [0.0]*40
for i in range (0, 40):
    notas [i] = float(input(f'Nota do {i+1}º aluno = '))
    soma += notas [i]

media = soma/40    

for i in range (0,40):
    if notas [i] > media:
        cont += 1

print('-'*90)
print(f'A média das notas igual à {media}, onde {cont} alunos a possuem.')
