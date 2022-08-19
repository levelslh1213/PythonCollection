class Dog:
    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade

class nha:
    def __init__(self) -> None:
        self.__numero = 5

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

teste = nha()

teste.numero = 10

teste.numero
