texto_simples = 'Simples é melhor do que complexo.'
texto_duplas = "Complexo é melhor do que complicado."

paragrafo = 'Primeira linha.\nSegunda linha.'
espacamento = 'Primeiro texto.\tSegundo texto.'

caminho = 'C:\nome\pasta'
escape_caminho = r'C:\nome\pasta'


print(f'''
*** Aspas ***
Simples: {texto_simples}
Duplas: {texto_duplas}

*** Caracteres de especiais ***
Parágrafo: {paragrafo}
Espaçamento: {espacamento}

** Ignorando caracteres especiais **
Caminho: {caminho}
Caminho: {escape_caminho}
      ''')