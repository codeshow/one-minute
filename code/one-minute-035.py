# *args e *kwargs

def listar_animais(*args):
    print(f'Listar:\n{args}\n')

listar_animais("Cachorro", "Gato", "Elefante", "Tigre")


def info_animal(**kwargs):
    print(f"Informar:\n{kwargs}")

info_animal(nome="Cachorro", cor="Marrom", habitat="Doméstico", idade=5)