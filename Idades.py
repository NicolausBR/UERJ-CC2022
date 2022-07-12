#Variável que define a idade a ser analisada pelo código.
idade = int(input('Identidade a ser analisada:'))

#Agora vamos definir as idades em alguns intevalos que são:
#Bebê, Criança, Adolescente, Jovem Adulto, Adulto e Idoso

if idade < 0:
    print('ERRO, não existe idade menor do que 0 cabeção')

elif idade <= 3:
    print('Bebê')
    
elif idade <= 11:
    print('Criança')

elif idade <= 17:
    print('Adolescente')

elif idade <=25:
    print('Jovem Adulto')

elif idade <=50:
    print('Adulto')

else:
    print('Idoso')

