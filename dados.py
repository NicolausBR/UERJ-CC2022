import random
dado = [1 , 2 , 3 , 4 , 5 , 6]
pares = 0
impares = 0

resp = str(input('Vamos jogar um jogo de dados meu casa? ')).upper()

if resp == 'S' or resp == 'SIM' or resp == 'BORA':
    pi = str(input('Beleza, vai escolher os números pares ou ímpares seu NOOB? ')).upper()
    
    if pi == 'PARES':
        aposta = 0

    else:
        aposta = 1
        
    quant = int(input('Vamos jogar quantos dados meu parceiro? '))
    print('')

    for i in range (0, quant):
        valor = random.choice(dado)
        
        if valor%2 == 0:
            pares += 1

        else:
            impares += 1

    if aposta == 0:
        if pares > impares:
            print('FDP HACKER LIXO TA ME ZOANDO? VENCER COM CÓDIGO ATÉ EU.')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

        elif pares == impares:
            print('Empate, que sem graça, chatão tu e esse jogo vlw falou.')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

        else:
            print('NOOB, achei fácil, troxa. Perdeste, os outros macacos comeram mais rápido!')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

    if aposta == 1:
        if pares > impares:
            print('NOOB, achei fácil, troxa. Perdeste, os outros macacos comeram mais rápido!.')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

        elif pares == impares:
            print('Empate, que sem graça, chatão tu e esse jogo vlw falou.')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

        else:
            print('FDP HACKER LIXO TA ME ZOANDO? VENCER COM CÓDIGO ATÉ EU.')
            print('-'*80)
            print(f'Pares = {pares}')
            print(f'Ímpares = {impares}')

elif resp == 'N' or resp == 'NÃO':
    print('CALA A BOCA PUTA!')
            
