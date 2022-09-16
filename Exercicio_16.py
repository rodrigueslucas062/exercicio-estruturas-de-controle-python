#Faça um programa que receba duas notas de seis alunos. Calcule e mostre:

qtdaprovados = 0
qtdreprovados= 0
qtdexame = 0
somamedia = 0

for i in range(1,7):
  notas = input(f'Digite as notas do {i}° aluno: ')
  conjuntonotas = notas.split('')
  medianotas = (int(conjuntonotas[0]) + int(conjuntonotas[1])) / 2
  somamedia += medianotas
  print(f'Média do {i}° aluno: {medianotas}')
  if medianotas < 30:
    situacao = 'Reprovado'
    qtdreprovados += 1
  elif medianotas < 70:
    situacao = 'Exame Especial'
    qtdexame += 1
  else:
    situacao = 'Aprovado'
    qtdaprovados += 1
print(f'Situação do aluno: {situacao}')
print(f'Quantidade de alunos reprovados: {qtdreprovados}\n')
print(f'Quantidade de alunos em Exame Especial: {qtdexame}\n')
print(f'Quantidade de alunos aprovados: {qtdaprovados}\n')
print(f'Média da turma: {somamedia / 6}')