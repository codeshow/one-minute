lista_compras = [
    'pão', 
    'frutas',
    'legumes',
    'verduras',
    ]

lista_compras = lista_compras + ['molhos']
lista_compras += ['massas']

posicao = lista_compras[0]
lista_compras[0] = 'pão integral'
posicao_atualizada = lista_compras[0]


print(f'''\
*** Atualização em listas ***
{'Lista de compras = ':25}{lista_compras}
{'Posição[0] = ':25}{posicao}
{'Posição[0] atualizada = ':25}{posicao_atualizada}
''')
