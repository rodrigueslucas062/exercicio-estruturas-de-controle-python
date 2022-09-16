#Faça um programa que receba vários números, calcule e mostre:

numeros = input('Digite os números, sem espaço: ')
narray = list(numeros)
soma = 0
qtdnumeros = len(narray)
maior = max(narray)
menor = min(narray)
somapar = 0
qtdpares = 0
qtdimpares = 0

for numero in narray:
  soma += int(numero)
  if int(numero) % 2 == 0:
    somapar += int(numero)
    qtdpares += 1
  else:
    qtdimpares += 1

media = soma / qtdnumeros
media_numeros_pares = somapar / qtdpares
porcentagem_de_impares = (qtdimpares * 100) / qtdnumeros

print(f'Soma: {soma}\n')
print(f'Quantidade de números digitados: {qtdnumeros}\n')
print(f'Média dos números: {media}\n')
print(f'Maior número: {maior}\n')
print(f'Menor número: {menor}\n')
print(f'Média dos números pares: {media_numeros_pares}\n')
print(f'Porcentagem de números ímpares: {porcentagem_de_impares}%')