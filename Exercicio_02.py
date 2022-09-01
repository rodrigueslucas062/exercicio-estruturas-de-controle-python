#Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir.

nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))

media = nota_1 + nota_2 + nota_3 / 3

if 7 <= media <= 10:
    print('Aprovado')
if 3 <= media <= 7:
    print('Exame especial')
if 0 <= media <= 3:
    print('Reprovado')