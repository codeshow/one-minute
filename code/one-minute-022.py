# Escopo
escopo = "Global"
acessivel = "Apenas uso"

def funcao():
    escopo = "Local"
    
    print(f'"escopo" dentro da função: {escopo}\nid: {id(escopo)}\n')

    print(f'"acessivel" dentro da função: {acessivel}\nid: {id(acessivel)}\n')

funcao()

print(f'"escopo" fora da função: {escopo}\nid: {id(escopo)}\n')
print(f'"acessivel" fora da função: {acessivel}\nid: {id(acessivel)}\n')
