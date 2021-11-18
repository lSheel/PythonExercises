#Si desea hacer una copia independiente de un objeto compuesto (lista, diccionario, instancia de clase personalizada),
# debe hacer uso de la copia profunda, que:
# construye un nuevo objeto compuesto y luego, recursivamente, inserta copias en él de los objetos encontrados
# en el original;
# tarda más en completarse, ya que hay muchas más operaciones por realizar;
# es implementado por la función deepcopy (), entregado por el módulo 'copy' de python

import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)


      ######SHALLOW######               #######DEEP########

#   A_LIST           B_LIST            A_LIST            B_LIST
#       \              /                 |                 |
#        \            /                  |                 |
#         \          /                   |                 |
#         ------------              ------------       ------------
#         | MEMORIA  |              | MEMORIA  |       | MEMORIA  |
#         ------------              ------------       ------------
