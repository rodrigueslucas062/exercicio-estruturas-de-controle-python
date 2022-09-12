#Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:

salario_inicio =  1000
aumento = 0.03
salario =  0
i = 5

while i <= 22:
    salario = (salario_inicio * 0.015) + salario_inicio
    salario_final = (salario * (aumento * 2) + salario + salario_inicio)
    i = i + 1
print(f'{salario_final}')
