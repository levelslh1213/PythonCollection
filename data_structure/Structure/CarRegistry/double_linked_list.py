from base64 import encode
from email import header
from lib2to3.pytree import Node
from .carro import car


class double_linked_list:
    def __init__(self):
        self.__head = None
        self.__size = 1

    def insert_element(self, node: car):
        if self.__head == None:
            self.__head = node
        else:
            if self.__head.prev == None:
                self.__head.prev = node
                self.__head.next = node
                node.next = self.__head
                node.prev = self.__head
            else:
                aux = self.__head.prev
                node.next = self.__head
                node.prev = aux
                aux.next = node
                self.__head.prev = node

    def print_list(self):
        aux = self.__head
        while (aux.next != self.__head):
            print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")
            aux = aux.next
        print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")

    def get_by_brand(self, brand: str):
        if self.__head.marca == brand:
            print(f"""
                    Carro: {self.__head.id}
                    -> {self.__head.marca}/{self.__head.modelo}""")

        aux = self.__head.next
        while (aux != self.__head):
            if aux.marca == brand:
                print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")
            aux = aux.next

    def get_by_id(self, id: str):
        if self.__head.id == id:
            print(f"""
                    Carro: {self.__head.id}
                    -> {self.__head.marca}/{self.__head.modelo}""")

        aux = self.__head.next
        while (aux.id != id):
            aux = aux.next
        print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")

    # Há algum forma de fazer esse condicionamento diretamente no laço de repetição
    # Intenção é não repetir o laço 3 vezes
    def get_by_price(self, condition: str, value: float, value2: float = 0):
        if condition == ">":
            if self.__head.valor >= value:
                print(f"""
                            Carro: {self.__head.id}
                            -> {self.__head.marca}/{self.__head.modelo}
                            -> {self.__head.valor}""")
        elif condition == "<":
            if self.__head.valor < value:
                print(f"""
                            Carro: {self.__head.id}
                            -> {self.__head.marca}/{self.__head.modelo}
                            -> {self.__head.valor}""")
        elif condition == "in":
            if value < self.__head.valor < value2:
                print(f"""
                            Carro: {self.__head.id}
                            -> {self.__head.marca}/{self.__head.modelo}
                            -> {self.__head.valor}""")

        aux = self.__head.next
        while (aux != self.__head):
            if condition == ">":
                if aux.valor >= value:
                    print(f"""
                            Carro: {aux.id}
                            -> {aux.marca}/{aux.modelo}
                            -> {aux.valor}""")
            elif condition == "<":
                if aux.valor < value:
                    print(f"""
                            Carro: {aux.id}
                            -> {aux.marca}/{aux.modelo}
                            -> {aux.valor}""")
            elif condition == "in":
                if value <= aux.valor <= value2:
                    print(f"""
                            Carro: {aux.id}
                            -> {aux.marca}/{aux.modelo}
                            -> {aux.valor}""")
            aux = aux.next

    def get_by_situation(self, situation):
        if self.__head.situacao == situation:
            print(f"""
                    Carro: {self.__head.id}
                    -> {self.__head.marca}/{self.__head.modelo}
                    -> {self.__head.situacao}""")

        aux = self.__head.next
        while(aux != self.__head):
            if aux.situacao == situation:
                print(f"""
                        Carro: {aux.id}
                        -> {aux.marca}/{aux.modelo}
                        -> {aux.situacao}""")
            aux = aux.next

    def get_values_to_external_font(self, filtro = None):
        if self.__size == 0:
            raise ValueError("Seu mula, vou nem falar nada...")
        else:
            self.__create_data_font(filtro)

    def __create_data_font(self, filtro = None):
        import pandas as pd
        tabela = {
            "id" : [ ],
            "marca" : [ ],
            "modelo" : [ ],
            "ano" : [ ],
            "valor" : [ ],
            "quilometragem" : [ ],
            "observacao" : [ ]
        }
        aux = self.__head.next
        tabela["id"].append(self.__head.id)
        tabela["marca"].append(self.__head.marca)
        tabela["modelo"].append(self.__head.modelo)
        tabela["ano"].append(self.__head.ano)
        tabela["valor"].append(self.__head.valor)
        tabela["quilometragem"].append(self.__head.quilometragem)
        tabela["observacao"].append(self.__head.observacao)

        while(aux != self.__head):
            tabela["id"].append(aux.id)
            tabela["marca"].append(aux.marca)
            tabela["modelo"].append(aux.modelo)
            tabela["ano"].append(aux.ano)
            tabela["valor"].append(aux.valor)
            tabela["quilometragem"].append(aux.quilometragem)
            tabela["observacao"].append(aux.observacao)
            aux = aux.next

        print(tabela)
        df_tabela = pd.DataFrame(tabela)
        if filtro != None:
            df_tabela = df_tabela[df_tabela["marca"] == filtro]
        print(df_tabela)
        nome_arquivo = input("Digite o nome do arquivo:")
        df_tabela.to_csv(f"data_structure\Exports\{nome_arquivo}.csv", ";", index=False, encoding="UTF-8")

