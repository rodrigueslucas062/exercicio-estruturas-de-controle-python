#Foi feita uma pesquisa para determinar o índice de mortalidade infantil em certo período. Faça um programa que:

nascimentos = int(input('Digite o número de crianças nascidas: '))
meninas = 0
meninos = 0
menor24 = 0

for i in range(1, (nascimentos +1)):
  sexo = input('Digite o sexo da criança (M ou F) e tempo de vida(meses): ')
  dados = sexo.split(' ')
  if int(dados[1]) <= 24:
      print('Menor')
      menor24 += 1
      print(menor24)
  if dados[0] == 'M':
    meninos += 1
  elif dados[0] == 'F':
    meninas += 1

porcentagemmenina = (meninas * 100) / nascimentos
porcentagemmenino = (meninos * 100) / nascimentos
menores24 = (menor24 * 100) / nascimentos

print(f'Meninas: {porcentagemmenina}%\n')
print(f'Meninos: {porcentagemmenino}%\n')
print(f'Porcentagem menor que 24 meses: {menores24}%\n')