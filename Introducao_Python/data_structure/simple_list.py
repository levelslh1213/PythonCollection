from email import header
from random import randint
from Structure.SimpleList import linear_list

array = linear_list()
for x in range(10):
    array.insert_element(x)
array.print_list()
