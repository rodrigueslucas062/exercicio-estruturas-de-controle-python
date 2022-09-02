#Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

import math

print('1) Somar dois números.\n2) Raiz quadrada de um número.')

entrada = int(input('Opção: '))

if entrada == 1:
    numero_1 = float(input('Número 1: '))
    numero_2 = float(input('Número 2: '))

    print(f' {numero_1 + numero_2}')

if entrada == 2:
    numero_2 = float(input('Número: '))

    print(f' {math.sqrt(numero_2)}')

if entrada != 1 or 2:
    print('Digite um número valido')
