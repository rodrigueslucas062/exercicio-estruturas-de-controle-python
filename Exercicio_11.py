#Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre a classificação dessa pessoa.

peso = float(input('Peso: '))
altura = float(input('Altura: '))

if altura < 120 and peso < 60:
    print('A')

if altura < 120 and (peso in range(60, 90)):
    print('D')

if altura < 120 and peso > 90:
    print('G')

if (altura in range(120, 170)) and peso < 60:
    print('B')

if (altura in range(120, 170)) and (peso in range(60, 90)):
    print('E')

if (altura in range(120, 170)) and peso > 90:
    print('H')

if altura > 170 and peso < 60:
    print('C')

if altura > 170 and (peso in range(60, 90)):
    print('F')
    
if altura > 170 and peso > 90:
    print('C')