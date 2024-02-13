lista_compras = [
    'pão', 
    'frutas',
    'arroz',
    'feijão',
    'café',
    'legumes',
    'verduras',
    ]
lista_original = lista_compras.copy()

lista_compras.remove('pão')
lista_remove = lista_compras.copy()

remove_ultimo = lista_compras.pop()
remove_index = lista_compras.pop(2)
remove_index_negativo = lista_compras.pop(-2)
lista_pop = lista_compras.copy()

lista_compras.clear()
lista_clear = lista_compras.copy()

print(f'''\
*** Remoção de elementos em listas ***
{'Lista de compras = ':25}
{'':3}{lista_original}
{'Remoção por remove= ':25}
{'':3}{lista_remove}
{'Retorno do último = ':23}{remove_ultimo}
{'Retorno do índice 2 = ':23}{remove_index}
{'Retorno do índice -2 = ':23}{remove_index_negativo}
{'Remoção por pop = ':25}
{'':3}{lista_pop}
{'Remoção de todos itens = ':25}{lista_clear}
''')
