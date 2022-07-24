import math

area = 0
semip = 0

lado1 = int(input('Primeiro lado do triângulo  = '))
lado2 = int(input('Segundo lado do triândulo = '))
lado3 = int(input('Terceiro lado do triângulo = '))
print('-'*40)

if lado1 <=0 or lado2 <=0 or lado3 <=0:
    print('O cálculo não será realizado, pois em ao menos um dos lados foi inserido um valor menor ou igual a 0')

else:
    #Semiperímetro = perímetro / 2.
    semip = (lado1+lado2+lado3)/2


    #Calcular a área usando o Teorema de Herão já que só temos a informação das lados:
    teorema = semip*(semip-lado1)*(semip-lado2)*(semip-lado3)

    if teorema <= 0:
        print('Não é possível calcular a área deste triangulo pois não existe solução nos números reais para ele ou sua área total é igaual a 0')

    else:
        area = math.sqrt(teorema)

        print(f'A área do triangulo com os lados medindo {lado1}, {lado2}, {lado3}, é igual a = {area}.')
