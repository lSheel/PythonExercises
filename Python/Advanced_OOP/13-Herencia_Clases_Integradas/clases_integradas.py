#Heredar propiedades de clases integradas
# Python le brinda la capacidad de crear una clase que hereda propiedades de cualquier clase incorporada de Python
# para obtener una nueva clase que pueda enriquecer los atributos o métodos de los padres.

class IntegerList(list):
    #Se crea un metodo estatico para validar si el tipo del valor es compatible
    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')
    #Se sobreescribe el metodo __setitem__ que es una metodo ya integrado 
    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 49
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')

print('Final result:', int_list)
