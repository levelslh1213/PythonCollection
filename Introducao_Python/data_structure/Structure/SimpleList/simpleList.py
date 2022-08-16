from .node import node


class linear_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_element(self, number):
        no = node(number, None)
        if self.size == 0:
            self.head = no
            self.size += 1
        else:
            aux = self.head
            while aux.next != None:
                aux = aux.next
            aux.next = no
            aux = no
            self.size += 1

    def print_list(self):
        aux = self.head
        while aux != None:
            print(aux.number)
            aux = aux.next

    # def insert_element_by_id(self, position):
