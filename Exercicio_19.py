#Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e positivos, um par de cada vez, e que calcule e mostre a soma de todos os números inteiros entre m e n (inclusive). A digitação de pares terminará quando m for maior ou igual a n.

def calculo():
  numeros = list(input('Digite um par de números: '))
  soma = 0
  if numeros[0] >= numeros[1]:
    return 'Fim'
  else:
    for i in range(int(numeros[0]), (int(numeros[1]) + 1)):
      soma += i
    return f'Soma entre de numeros X e Y: {soma}'
calculo()