#A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:


laboratorio = float(input('Nota laboratorio: '))
semestral = float(input('Nota semestral: '))
exame = float(input('Nota exame: '))

peso_laboratorio = 2
peso_semestral = 3
peso_exame = 5

media = laboratorio / peso_laboratorio + semestral / peso_semestral + exame / peso_exame

if 8 <= media <= 10:
    print(f'A')
if 7 <= media <= 8:
    print(f'B')
if 6 <= media <= 7:
    print(f'C')
if 5 <= media <= 6:
    print(f'D')
if 0 <= media <= 5:
    print(f'E')