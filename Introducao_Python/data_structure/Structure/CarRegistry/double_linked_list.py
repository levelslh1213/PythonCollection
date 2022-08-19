from lib2to3.pytree import Node
from .carro import car

class double_linked_list:
    def __init__(self):
        self.__head = None
        self.size = 0

    def insert_element(self, node : car):
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
        while(aux.next != self.__head):
            print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")
            aux = aux.next
        print(f"""
                    Carro: {aux.id}
                    -> {aux.marca}/{aux.modelo}""")