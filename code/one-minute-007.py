texto = 'Python Brasil'
tamanho = len(texto)
# texto[start:stop:step]
pares = texto[::2]
invertido = texto[::-1]


print(f'''\
*** Accessando subtextos ***
{'Texto = ':13}{texto}
{'Tamanho = ':13}{tamanho}
{'Pares = ':13}{pares}
{'Invertido = ':13}{invertido}
''')
