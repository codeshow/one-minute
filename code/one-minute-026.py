# Estrutura de dados: Filas FIFO
from collections import deque

fila = deque(['a', 'b', 'c'], maxlen=5)
fila.append('d')
fila.append('e')

print(f""" *** Filas ***
fila: {fila}
fila.pop(): {fila.popleft()}
fila.pop(): {fila.popleft()}
fila.pop(): {fila.popleft()}
fila.pop(): {fila.popleft()}
fila: {fila}
""")
