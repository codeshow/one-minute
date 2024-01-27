lista_compras = [
    'pão', 
    'frutas',
    'legumes',
    'verduras',
    ]

primeiro_item = lista_compras[0]
ultimo_item = lista_compras[-1]
parte_lista = lista_compras[1:3]
pares_lista = lista_compras[::2]
# [start:stop:step]


print(f'''\
*** Acesso em listas ***
{'Lista de compras = ':25}{lista_compras}
{'Primeiro item = ':25}{primeiro_item}
{'Último item = ':25}{ultimo_item}
{'Parte da lista = ':25}{parte_lista}
{'Pares da lista = ':25}{pares_lista}
{'Tipo item individual = ':25}{type(ultimo_item)}
{'Tipo varios itens = ':25}{type(pares_lista)}
''')

