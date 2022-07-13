#O programa busca fazer a média entre 2 notas dos alunos e dividir em dois grupos, masculino e feminino, para no fim mostrar a média nesses grupos

contm = 0
contf = 0
somm = 0
somf = 0
nome = str(input('Nome do Aluno(a):(X para fechar o Programa)'))

while (nome != 'X') and (nome !='x'):
    sexo = input( '"M" para masculino ou "F" para feminino:')
    if sexo == 'M' or sexo == 'm':
        n1 = float(input('Primeira Nota:'))
        n2 = float(input('Segunda Nota:'))
        pmedia = (n1+n2)/2
        contm = contm + 1
        somm = somm + pmedia   

    elif sexo == 'F' or sexo == 'f':
        n1 = float(input('Primeira Nota:'))
        n2 = float(input('Segunda Nota:'))
        pmedia = (n1+n2)/2
        contf = contf +1
        somf = somf + pmedia

    else:
        print('ERRO, tente novamente')

    if contm != 0:
        print('')
        print('Média dos Homens:', somm/contm)
        
    if contf != 0:
        print('')
        print('Média das Mulheres:', somf/contf)

    nome = str(input('Nome do Aluno(a):(X para fechar o Programa)'))
        
                
