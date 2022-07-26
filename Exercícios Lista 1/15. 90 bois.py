boimaior = 0
boimaiorn = str 
boimenor = 9999
boimenorn = str

print('OBS: Caso dois ou mais bois tenham o mesmo peso(Kg), apenas o primeiro a ser inserido será contabilizado caso seja o maior ou o menor!')
print('')
for boi in range(1,91):
    name = str(input(f'Nome do {boi}º boi: '))
    peso = float(input(f'Peso do {boi}º boi: '))
    print('-'*50)

    if peso > boimaior:
        boimaiorn = name
        boimaior = peso

    if peso < boimenor:
        boimenorn = name
        boimenor = peso

    
print(f'O boi com maior peso tem {boimaior}Kg, com o nome de {boimaiorn}.')
print(f'O boi com menor peso tem {boimenor}Kg, com o nome de {boimenorn}.')
