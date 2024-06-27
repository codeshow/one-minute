lista = [1, 2, 3, 4, 5]

print("if a or b in lista:")
def verifica_se_esta_na_lista(a, b):
    if a or b in lista:
        print("Sim")
    else:
        print("Não")

print("Retorna 'Sim' nos casos de False ou True | True ou False | True ou True")
verifica_se_esta_na_lista(2, 4)
verifica_se_esta_na_lista(2, 40)
verifica_se_esta_na_lista(20, 40)

print("Retorna 'Não' nos casos de False ou False")
verifica_se_esta_na_lista(0, 0)
verifica_se_esta_na_lista('', '')
verifica_se_esta_na_lista(None, None)
