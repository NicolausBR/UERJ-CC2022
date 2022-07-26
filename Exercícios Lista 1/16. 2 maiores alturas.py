maior1 = 0
maior2 = 0

nome = str(input('Nome da senhorita: ')).upper
while nome != 'MARIA':
    altura = float(input('Altura da senhorita em cm = '))

    if altura > maior1:
        maior1 = altura

    elif altura > maior2:
        maior2 = altura
