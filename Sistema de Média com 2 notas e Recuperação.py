#Código para fechar o programa só quando o usuário digitar X
sair = str(input('Insira X caso deseje fechar o programa:'))

#Caso o usuário não queira sair, o código cai continuar rodando.

while ((sair != 'x') and (sair != 'X')):

#Código para inserir as médias e logo após analisar os casos de Aprovado ou Reprovado.
    
    nota1 = float(input('Primeira Nota:'))
    nota2 = float(input('Segunda Nota:'))
    media = float(nota1+nota2)/2

    if media >= 7:
            print('')
            print('Parabéns, você foi aprovado! Sua média:',media)


    else:
        print('')
        print('Você não foi aprovado. Sua média:',media)
        print('')
        nota_r = float(input('Nota de Recuperação para nova média:'))
        media_r = (media+nota_r)/2

        if media_r >=7:
            print('')
            print('Parabéns, sua nova média de',media_r,' o aprovou.')

        else:
            print('')
            print('Você não alcançou a média necessária, mais sorte na próxima vez. Sua média :',media_r)
            10
    print('')
    sair = input('Insira X caso deseje fechar o programa:')

