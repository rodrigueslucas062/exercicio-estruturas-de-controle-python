#Faça um programa que receba o salário inicial de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e de auxílio escola.


salario = int(input('Salário: '))

if salario < 499:
    aumento = int (salario + (escriturario * salario))
    print(f'O salario atual é de: {salario}, e o aumento é de: {aumento}. O novo salario é de: {salario + aumento}')