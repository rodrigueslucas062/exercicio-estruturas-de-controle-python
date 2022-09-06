#Faça um programa que receba o salário inicial de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e de auxílio escola.


salario = int(input('Salário: '))

if salario < 500:
    bonificacao = int (salario + (salario * 0.05))
    print(f'O salario atual é de: {salario}, e o bonificacao é de: {bonificacao}. O novo salario é de: {bonificacao + 150} com auxilio escola')

if (salario in range(600, 1200)):
    bonificacao = int (salario + (salario * 0.12))
    print(f'O salario atual é de: {salario}, e o bonificacao é de: {bonificacao}. O novo salario é de: {bonificacao + 100} com auxilio escola')
    
if salario > 1200:
    print(f'O salario atual é de: {salario + 100}, e não possui bonificação')