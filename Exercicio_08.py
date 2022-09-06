#Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado, o produto deve preencher pelo menos um dos requisitos a seguir:

vendas = int(input('Vendas: '))
preco = float(input('Preço: '))

if vendas < 500 and preco < 30:
    novo = preco * 0.3
    print(f'{preco + novo}')

if vendas in range(500, 1200) and preco >= 30 < 80:
    novo = preco * 0.15
    print(f'{preco + novo}')

if vendas >= 1200 and preco >= 80:
    novo = preco * 0.2
    print(f'{preco - novo}')