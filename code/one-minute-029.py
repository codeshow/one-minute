# List comprehensions - aninhadas
matriz = [
    [j for j in range(3)]
    for i in range(3)]


# for aninhado
matriz_for = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(j)
    matriz_for.append(linha)


print(f"""
Matriz list comp:
{matriz}
Matriz for aninhado:
{matriz_for}
""")
