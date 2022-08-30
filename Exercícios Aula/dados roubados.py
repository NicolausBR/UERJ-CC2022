import random
tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
tot5 = 0
tot6 = 0

quant = int(input('Quantos dados?'))

for i in range (0, quant):
    num = random.choice([1,2,2,2,3,4,5,6])

    if num == 1:
        tot1 += 1

    elif num == 2:
        tot2 += 1

    elif num == 3:
        tot3 += 1

    elif num == 4:
        tot4 += 1

    elif num == 5:
        tot5 += 1

    else:
        tot6 += 1

print('-'*100)
print(f'Dados com valor 1 = {tot1}')
print(f'Porcentagem = {(tot1/quant)*100}%')

print('-'*100)
print(f'Dados com valor 2 = {tot2}')
print(f'Porcentagem = {(tot2/quant)*100}%')

print('-'*100)
print(f'Dados com valor 3 = {tot3}')
print(f'Porcentagem = {(tot3/quant)*100}%')

print('-'*100)
print(f'Dados com valor 4 = {tot4}')
print(f'Porcentagem = {(tot4/quant)*100}%')

print('-'*100)
print(f'Dados com valor 5 = {tot5}')
print(f'Porcentagem = {(tot5/quant)*100}%')

print('-'*100)
print(f'Dados com valor 6 = {tot6}')
print(f'Porcentagem = {(tot6/quant)*100}%')
