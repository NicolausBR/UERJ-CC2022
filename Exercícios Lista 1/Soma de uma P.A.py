termo1 = int(input('Termo inicial da P.A. :'))
razao = int(input('Razão da P.A. :'))
n = int(input('Quantos termos a serem calculados?:'))
soma = 0

#Fórmula para encontrar a P.A. aplicada em python:

ultimo = termo1 + (n-1)*razao

for var in range (termo1, ultimo+1, razao):
    print(var)
    soma += var

print('Soma da P.A. =', soma)
