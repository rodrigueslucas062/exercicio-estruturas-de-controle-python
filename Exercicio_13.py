#Escreva um programa que calcule o quadrado e o cubo dos números de 0 a 10, e imprima os valores em forma de tabela. Número | Quadrado | Cubo
import math
i = 1

print("numero \t quadrado \t cubo\n")
while i <= 10:
    print(f'{i} \t {i*i} \t {i*i*i}') 
    i = i + 1