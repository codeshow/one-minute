entrada = 10

certo = entrada == 10
errado = entrada != 10
maior = entrada > 10
maior_igual = entrada >= 10
menor = entrada < 10
menor_igual = entrada <= 10



print(f'''\
      *** Operadores de comparação ***
        {'Entrada = ':22}{entrada}
        {'Igual a 10 = ':22}{certo}
        {'Diferente de 10 = ':22}{errado}
        {'Maior que 10 = ':22}{maior}
        {'Maior ou igual a 10 = ':22}{maior_igual}
        {'Menor que 10 = ':22}{menor}
        {'Menor ou igual a 10 = ':22}{menor_igual}
        ''')
