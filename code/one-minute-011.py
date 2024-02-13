lista_compras = [
    'pão', 
    'frutas',
    ]
lista_original = lista_compras.copy()

lista_compras.append('vinho')
lista_append = lista_compras.copy()

lista_compras.insert(2, 'molhos')
lista_insert = lista_compras.copy()

lista_compras.extend(
    ['bolo', 'arroz']
    )
lista_compras.extend(
    ('doces', 'salgados')
    )
lista_compras.extend(
    {'massas', 'biscoitos'}
    )
lista_extend = lista_compras.copy()

print(f'''\
*** Atualização em listas ***
{'Lista original = ':17}{lista_original}
{'Lista append = ':17}{lista_append}
{'Lista insert = ':17}{lista_insert}
{'Lista extend = ':17}{lista_extend}
''')
