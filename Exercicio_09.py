#Faça um programa para resolver equações do 2º grau.

import math

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

delta = b**2 - 4 * a * c 

if delta < 0:
    print(f'Não existe raiz real{delta}')

if delta == 0:
    print(f'Existe raiz real {delta}')

if delta > 0:
    x1 = -b + (math.sqrt (delta)) / 2 * a
    x2 = -b - (math.sqrt (delta)) / 2 * a 
    print(f'As raizes são: {x1} e {x2}')
