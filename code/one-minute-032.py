# Expressão lambda

# lambda arg_1, arg_2: expressão
soma_lambda = lambda a, b: a + b

def soma(a, b):
    return a + b


print(f""" **** Expressão lambda ****
lambda 1 + 2:
{soma_lambda(1,2)}

função 1 + 2:
{soma(1,2)}
""")
