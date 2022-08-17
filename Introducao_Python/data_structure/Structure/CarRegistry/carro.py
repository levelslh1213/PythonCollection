class car:
    def __init__(self,
                 id: int,
                 marca: str,
                 modelo: str,
                 ano: int,
                 valor: float,
                 quilometragem: int,
                 observacao: str = "",
                 next = None,
                 prev = None):
        self.__id = self.trata_id(id)
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__valor = valor
        self.__quilometragem = quilometragem
        self.__observacao = observacao
        self.__next = next
        self.__prev = prev

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = self.trata_id(value)

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def valor(self):
        return self.__valor

    @property
    def quilometragem(self):
        return self.__quilometragem

    @quilometragem.getter
    def quilometragem(self):
        return str(self.__quilometragem) + " Km"

    @property
    def situacao(self):
        if self.__quilometragem == 0:
            return "Novo"
        elif self.__quilometragem <= 20000:
            return "Semi-Novo"
        elif self.__quilometragem > 20000:
            return "Usado"

    @property
    def observacao(self):
        return self.__observacao

    @observacao.getter
    def observacao(self):
        return "Observação: " + self.__observacao
    
    @property
    def next(self):
        return self.__next
    @property
    def prev(self):
        return self.__prev

    def trata_id(self, value):
        if len(value) == 3:
            return "02" + value
        else:
            print(f"Id precisa de 3 dig! {value}")
            return "00000"