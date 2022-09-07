#Faça um programa que receba:

origem = int(input('País de origem: '))
codigo = int(input('Código: '))
peso = int(input('Peso: '))

if (codigo in range (1, 10)) and (origem in range(1, 3)):
    if origem == 1 and codigo in range(1, 4):
        imposto = (peso / 1000) * 10
    print(f'{imposto}')

    if origem == 2 and codigo in range(5, 7):
        imposto = (peso / 1000) * 25 + (peso * 0.15)
    print(f'{imposto}')

    if origem == 3 and codigo in range(8, 10):
        imposto = (peso / 1000) * 10 + (peso * 0.25)
    print(f'{imposto}')
else: 
    print ('Invalido')
