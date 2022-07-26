sim = 0
nao = 0
homemsim = 0
mulhersim = 0
homemnao = 0
mulhernao = 0
homens = 0
mulheres = 0

for pessoa in range (1,2001):
    sexo = str(input('H = Homem / M = Mulher: ')).upper()

    if sexo == 'H':
        resph = str(input('Você gostou do produto? [S/N]: ')).upper()
        print('-'*40)
        homens += 1
        
        if resph == 'S':
            sim += 1
            homemsim += 1

        elif resph == 'N':
            nao += 1
            homemnao += 1

        else:
            print('Erro, essa pessoa não será contabilizada no cálculo final, tente novamente.')
            print('-'*40)
            homens -=1

    elif sexo == 'M':
        respm = str(input('Você gostou do produto? [S/N]')).upper()
        print('-'*40)
        mulheres += 1

        if respm == 'S':
            sim += 1
            mulhersim += 1

        elif respm == 'N':
            nao += 1
            mulhernao += 1

        else:
            print('Erro, essa pessoa não será contabilizada no cálculo final, tente novamente.')
            print('-'*40)
            mulheres -= 1

    else:
        print('Erro, essa pessoa não será contabilizada no cálculo final, tente novamente.')
        print('-'*40)

        
total = sim+nao
print('-'*50)
print(f'{sim} pessoas responderam que gostam do produto.')
print(f'{nao} pessoas responderam que não gostam do produto.')
print('-'*50)
print(f'{(homemnao/total)*100:.2f}% de homens com feedback negativo (Do total de pessoas)')
        
