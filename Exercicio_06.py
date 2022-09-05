#Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.

escriturario = 0.5
secretario = 0.35
caixa = 0.2
gerente = 0.1

print('Selecione uma opção:\n1) Escrituário\n2) Secretário/n3) Caixa\n4) Gerente\n5) Diretor')

entrada = int(input('Opção: '))

if entrada == 1:
    salario = float(input('Sálario: '))
    aumento = int (escriturario + (escriturario * salario))
    print(f'O salario atual é de: {salario}, e o aumento é de: {aumento}. O novo salario é de: {salario + aumento}')

if entrada == 2:
    salario = float(input('Sálario: '))
    aumento = secretario + (secretario * salario)
    print(f'O salario atual é de: {salario}, e o aumento é de: {aumento}. O novo salario é de: {salario + aumento}')

if entrada == 3:
    salario = float(input('Sálario: '))
    aumento = caixa + (caixa * salario)
    print(f'O salario atual é de: {salario}, e o aumento é de: {aumento}. O novo salario é de: {salario + aumento}')

if entrada == 4:
    salario = float(input('Sálario: '))
    aumento = gerente + (gerente * salario)
    print(f'O salario atual é de: {salario}, e o aumento é de: {aumento}. O novo salario é de: {salario + aumento}')

if entrada == 5:
    salario = float(input('Sálario: '))
    print(f'O salario atual é:{salario}, mas não possui aumento')