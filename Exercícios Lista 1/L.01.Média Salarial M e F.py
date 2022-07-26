homens = 0
mulheres = 0
saltotalm = 0
saltotalf = 0
salario30 = 0


iniciar = str(input('Digite "X" para terminar o programa.'))
while iniciar != "x" and iniciar !="X":
    sexo = str(input('"M" para masculino e "F" para feminino:'))

    if sexo == "F" or sexo == "f":
        idadef = int(input('Idade:'))
        salariof = float(input('Salário:'))
        if idadef < 30 and salario30 < salariof:
            salario30 = salariof
                
        saltotalf = saltotalf + salariof
        mulheres = mulheres + 1
        

    elif sexo == 'M' or sexo == 'm':
        idadem = int(input('Idade:'))
        salariom = float(input('Salário:'))
        if idadem < 30 and salario30 < salariom:
            salario30 = salariom
        
        saltotalm = saltotalm + salariom
        homens = homens +1

    else:
        print('ERRO, insira o Gênero novamente')

    if homens > 0:
        print('Média Salarial dos Homens = ', saltotalm/homens)
        print('')
    if mulheres > 0:
        print('Média Salarial das Mulheres =', saltotalf/mulheres)
        print('')
    print('Maior Salário encontrado entre pessoas com menos de 30 anos =',salario30)
    iniciar = str(input('Digite "X" para terminar o programa.'))

