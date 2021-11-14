#Métodos de clase
# Los métodos de clase son métodos que, al igual que las variables de clase, funcionan en la clase misma y
# no en los objetos de clase de los que se crea una instancia. Puede decir que son métodos vinculados a la
# clase, no al objeto.

#Convención
# Para poder distinguir un método de clase de un método de instancia, el programador lo señala
# con el decorador @classmethod que precede a la definición del método de clase.
# Además, el primer parámetro del método de clase es cls, que se utiliza para hacer referencia
# a los métodos y atributos de clase.

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())