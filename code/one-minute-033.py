# Expressão lambda
maior = lambda a, b: a if a > b else b

lista = [1,2,3,4,5]
contem = lambda x: x in lista

verifica_int = lambda n: type(n) is int


print(f""" ****lambda e diferentes expressões ****
maior(5,8):         {maior(5,8)}
maior(10,2):        {maior(10,2)}
contem(7):          {contem(7)}
contem(1):          {contem(1)}
verifica_int(1):    {verifica_int(1)}
verifica_int(5.7):  {verifica_int(5.7)}
""")
