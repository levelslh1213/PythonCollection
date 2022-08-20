from data_structure.Structure.CarRegistry.double_linked_list import double_linked_list
from data_structure.Structure.CarRegistry.carro import car

double_list = double_linked_list()
array = ['ford', 'chevrolet', 'kia', 'hyundai', 'audi']

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
node = car('000', 'audi', 'carro000', 0000, 0, 0, 'Sistro de Leilão')
double_list.insert_element(node)
node = car('001', 'ford', 'carro001', 2005, 10000, 200000, 'nha')
double_list.insert_element(node)
node = car('002', 'chevrolet', 'carro002', 2015, 15000, 10000, 'nha')
double_list.insert_element(node)
node = car('003', 'kia', 'carro003', 2019, 80000, 10000, 'nha')
double_list.insert_element(node)
node = car('004', 'hyundai', 'carro004', 2017, 55000, 25000, 'nha')
double_list.insert_element(node)
node = car('005', 'audi', 'carro005', 2001, 21500, 158400, 'nha')
double_list.insert_element(node)
node = car('006', 'audi', 'carro006', 2016, 136900, 18500, 'nha')
double_list.insert_element(node)
double_list.print_list()
double_list.get_by_brand('audi')
double_list.get_by_id("02006")
double_list.get_by_price(">", 100000)
double_list.get_by_price("<", 20000)
double_list.get_by_price("in", 50000, 80000)
double_list.get_by_situation("Novo")