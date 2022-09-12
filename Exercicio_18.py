#Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math

entrada = 1

entrada = int(input("Digite um número para calcular, para sair digite um numero menor ou igual a zero"))

while entrada > 0:    
    quadrado = entrada**2    
    cubo = entrada**3     
    raiz = math.sqrt(entrada)
    if entrada >= 0: 
        print(f"O quadrado é: {quadrado}")
        print(f"O cubo é: {cubo}") 
        print(f"A raiz é: {raiz}")
    else:
        print('Programa encerrado')