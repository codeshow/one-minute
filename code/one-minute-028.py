# List comprehensions
# Sequência com range
simples = [numero for numero in range(5)]

# Pares com condicional if
pares = [numero for numero in range(5)
    if numero % 2 == 0]

# Dobro com operação matematica
dobro = [numero*2 for numero in range(5)]


print(f""" *** Listas ***
Sequencia:  {simples}
Pares:      {pares}
Dobro:      {dobro}
""")
