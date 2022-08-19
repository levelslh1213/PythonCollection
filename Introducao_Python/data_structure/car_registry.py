from Introducao_Python.data_structure.Structure.CarRegistry.double_linked_list import double_linked_list
from Introducao_Python.data_structure.Structure.CarRegistry.carro import car

double_list = double_linked_list()
array = ['ford', 'chevrolet', 'kia']

"""
for marca in array:
    for id in range(3):
        node = car(id,
                   marca,
                   'carro' + str(id),
                   2010,
                   10000,
                   1000,
                   'pinto')
        double_list.insert_element(node)
"""

node = car('001', 'ford', 'carro001', 2010, 10000, 1000, 'nha')
double_list.insert_element(node)
node = car('002', 'chevrolet', 'carro002', 2010, 10000, 1000, 'nha')
double_list.insert_element(node)

double_list.print_list()
