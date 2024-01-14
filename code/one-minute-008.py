lista = ['tipo', 'lista']
lista_inteiro = [1, 2, 3, 4]
lista_float = [1.1, 2.2, 3.3, 4.4]
lista_string = [
    'um', 'dois', 'três', 'quatro'
    ]
lista_mista = [1, 2.2, 'três', 4.4,]

print(f'''\
*** Listas ***
{'Tipo Lista = ':20}{type(lista)}
{'Lista de inteiros = ':20}{lista_inteiro}
{'Lista de floats = ':20}{lista_float}
{'Lista de strings = ':20}{lista_string}
{'Lista mista = ':20}{lista_mista}
''')
