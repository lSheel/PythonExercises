#La misma información almacenada en __class__ podría recuperarse llamando a una función type ()
# con un argumento:

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))

#Cuando se llama a la función type () con tres argumentos, crea dinámicamente una nueva clase.
# Para la invocación de tipo (,,):
#
# El argumento especifica el nombre de la clase; Este valor se convierte en el atributo __name__ de la clase;
# El argumento especifica una tupla de las clases base de las que se hereda la clase recién creada; Este argumento
#       se convierte en el atributo __bases__ de la clase;
# El argumento especifica un diccionario que contiene definiciones de métodos y variables para el cuerpo de la
# clase; los elementos de este argumento se convierten en el atributo __dict__ de la clase y establecen el
#       espacio de nombres de la clase.

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)