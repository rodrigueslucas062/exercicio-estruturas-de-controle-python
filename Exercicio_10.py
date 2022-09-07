#Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem. Considere que:

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a == b == c:
    print('equilatero')

elif a!=b and b!=c and a!=c:
    print('escaleno')

else:
    print('isoceles')