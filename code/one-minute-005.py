concatena_operador = 'Um texto ' + 'mais outro'
concatena_textos = 'Code' 'Show'
concatena_linhas = ('Casos especiais não são '
                    'especiais o suficiente '
                    'para quebrar as regras.')

texto_formatado = '''\
- Plano é melhor do que denso               primeira
- Legibilidade conta                        segunda
- Erros nunca devem passar silenciosamente  terceira
'''

print(f'''\
*** Concatenação com operador ***
{concatena_operador}

*** Concatenação textos***
{concatena_textos}

*** Concatenação linhas***
{concatena_linhas}

*** Texto formatado ***
{texto_formatado}
      ''')