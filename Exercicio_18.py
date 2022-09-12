#Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math

q=0
c=0
r=0

entrada = 1

while entrada > 0:      
    entrada= int(input("Digite um número para que seja feito o seu quadrado, o cubo e a raiz "))
    saida = float(input("Para sair do programa digite um número negativo ou zero.")) 

if saida > 0:     
    q = entrada**2    
    c = entrada* entrada*entrada      
    r = entrada ** (1/2) 
print("\nO numero ao quadrado é: ", q)
print("\nO numéro ao cubo é: ", c) 
print("\nA raiz quadrada é: ", r)