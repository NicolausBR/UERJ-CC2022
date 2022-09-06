quant = 0

tempC = []
tempF = []

acimaf = 0
listaf = []

acimac =0
listac = []

somaC = 0
somaF = 0


for i in range (1,51):
    cel = float(input(f'Insira o valor da {i}° temperatura em °C: '))
    fah = (cel*1.8)+32
    tempC.append(cel)
    tempF.append(fah)
    quant +=1
    somaC += cel
    somaF += fah

mtempC = somaC/quant
mtempF = somaF/quant


for x in range (0, len(tempF)):
    if tempF[x] > mtempF:
        acimaf += 1
        listaf.append(tempF[x])

for x in range (0, len(tempC)):
    if tempC[x] > mtempF:
        acimac += 1
        listac.append(tempC[x])

print('-'*100)
print(f'A média das temperaturas em Celsius é = {mtempC}')
print(f'{acimac} temperaturas estão acima da média de Farenheit')
if len(listac) == 0:
    print('Nenhuma temperatura em Celsius é maior que a média da Farenheit')
else:
    print(f'{listac} são as temp. em °C maiores que a média de Farenheit')

print('')
print(f'A média das temperatura(s) em Farenheit é = {mtempF}')
print(f'{acimaf} temperatura(s) em Farenheit está(ão) acima da média de Farenheit')
print(f'{listaf} são as temp. em °F maiores que a média de Farenheit')
