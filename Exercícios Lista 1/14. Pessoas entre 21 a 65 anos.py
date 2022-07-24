#O grupo 1 será das pessoas que queremos obter a média (21<x<6)

grupo1 = 0
grupo2 = 0
somaidade = 0

idade = int(input('Insira a idade da pessoa:'))
print('-'*50)

if idade == int(-1):
    somaidade += idade
    grupo2 += 1
    
while idade != int(-1):

    if idade > 21 and idade < 65:
        grupo1 += 1
        somaidade += idade

    elif idade <0:
        print('Erro, não existe pessoa com idade negativa, tente novamente.')
        print('-'*50)
        
    else:
        grupo2 += 1
        somaidade += idade
        
    idade = int(input('Insira a idade da pessoa:'))
    print('-'*50)

total = grupo1+grupo2
mediatotal = somaidade/total
porcgrupo1 = (grupo1/total)*100

print(f'A média das idades encontrada foi de {mediatotal}')
print('-'*50)
print(f'Porcentagem de pessoas que estão entre as idades de 21 a 65 anos é de: {porcgrupo1:.2f}%.')
