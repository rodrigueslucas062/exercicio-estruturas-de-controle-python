#Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math

numero = 1
while numero >= 1: 
    numero = int(input('Digite um número: '))
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz = math.sqrt(numero)
    print(f'Número: {numero}\n Seu quadrado: {quadrado}\n Seu cubo: {cubo}\n Raiz quadrada: {raiz}')