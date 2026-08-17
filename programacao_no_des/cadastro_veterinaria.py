class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        pass


class Cachorro(Animal):

    def emitir_som(self):
        return "Au Au!"


class Gato(Animal):

    def emitir_som(self):
        return "Miau!"


# Exemplo de cadastro e uso do polimorfismo
pacientes = [
    Cachorro("Rex", 3),
    Gato("Mimi", 2),
    Cachorro("Bob", 5),
]

for animal in pacientes:
    print(
        f"Paciente: {animal.nome} | Idade: {animal.idade} anos | Som: {animal.emitir_som()}"
    )
