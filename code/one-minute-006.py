texto = 'CodeShow'
tamanho = len(texto)
primeira_letra = texto[0]
ultima_letra = texto[-1]
primeira_palavra = texto[0:4]
ultima_palavra = texto[4:8]
meio_texto = texto[2:6]


print(f'''\
*** Acessando subtextos ***
{'Texto = ':20}{texto}
{'Tamanho = ':20}{tamanho}
{'Primeira letra = ':20}{primeira_letra}
{'Última letra = ':20}{ultima_letra}
{'Primeira palavra = ':20}{primeira_palavra}
{'Última palavra = ':20}{ultima_palavra}
{'Meio do texto = ':20}{meio_texto}
''')
