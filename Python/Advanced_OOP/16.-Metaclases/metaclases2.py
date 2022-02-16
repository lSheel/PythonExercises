#Deberíamos familiarizarnos con algunos atributos especiales:
# __name__ - inherente a las clases; contiene el nombre de la clase;
# __class__ - inherente tanto para clases como para instancias; contiene información sobre la clase a la que
#       pertenece una instancia de clase;
# __bases__ - inherente a las clases; es una tupla y contiene información sobre las clases base de una clase;
# __dict__ - inherente tanto para clases como para instancias; contiene un diccionario (u otro tipo de objeto de
#       mapeo) de los atributos del objeto.

class Dog:
    pass

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is  ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('object "dog" attributes:', dog.__dict__)


