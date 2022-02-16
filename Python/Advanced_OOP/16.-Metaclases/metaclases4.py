#Ejemplo donde se crea dinámicamente una clase completamente funcional
#La clase Dog ahora está equipada con dos métodos (feed () y bark ()) y el atributo de instancia age.

def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

#Esta forma de crear clases, usando la función type, es sustancial para la forma en que Python crea clases
# usando la instrucción de clase:
# - Una vez que se ha identificado la instrucción de clase y se ha ejecutado el cuerpo de la clase,
#       se ejecuta el código class = type (,,);
# - El tipo es responsable de llamar al método __call__ al crear la instancia de clase; este método llama a otros dos métodos:
#       ° __new __ (), responsable de crear la instancia de clase en la memoria de la computadora; este método se
#       ejecuta antes de __init __ ();
#       ° __init __ (), responsable de la inicialización del objeto.

#Las metaclases generalmente implementan estos dos métodos (__init__, __new__), tomando el control del procedimiento
# de creación e inicialización de una nueva instancia de clase. Las clases reciben una nueva capa de lógica.