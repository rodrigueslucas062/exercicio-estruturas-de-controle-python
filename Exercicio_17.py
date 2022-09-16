#Faça um programa para calcular a área de um triângulo e que não permita a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

base = int(input("Base: "))
altura = int(input("Altura: "))

if base <= 0 or altura <= 0:
  print("Valores precisam ser maiores que 0")
else:
  area = (base*altura) / 2
  print(area)