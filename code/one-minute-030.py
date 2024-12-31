# Instrução del
compras = [
    "banana",
    "maçã",
    "pera",
    "abacate"
]
del compras[2]

cores = [
    "azul",
    "amarelo",
    "preto",
    "vermelho",
    "verde",
    "cinza"
]
del cores[1::2]


print(f""" **** Instrução del ****
Lista compras:
{compras}
Lista cores:
{cores}
""")
