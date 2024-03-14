texto = 'Texto inicial'

if True:
    texto = 'Dentro do bloco if'
elif False:
    texto = 'Dentro do bloco elif'
else:
    texto = 'Dentro do bloco else'
    if True:
        texto = 'Dentro do bloco if do else'

texto = 'Fora do bloco if'
normal = 'Volta ao fluxo normal'
