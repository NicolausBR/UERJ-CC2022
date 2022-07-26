total = 0

valor = float(input('Valor das Parcelas em R$ = ')) 
par = int(input('Em quantas parcelas serão pagas? '))
juros = float(input('Taxa de juros em % = '))/100
print('-'*50)

for i in range (1,(par+1)):
    x = (valor)/(1+juros)**i
    total += x

print(f'Ao total, será pago um valor de R$ {total:.2f} nesse financiamento')
