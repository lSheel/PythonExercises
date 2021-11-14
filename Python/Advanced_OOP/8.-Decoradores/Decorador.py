#Decorators are used in:

#the validation of arguments;
#the modification of arguments;
#the modification of returned objects;
#the measurement of execution time;
#message logging;
#thread synchronization;
#code refactorization;
#caching.

#Como puede ver, la definición de la función simple_hello () está literalmente decorada con '@simple_decorator',
# ¿no es una buena sintaxis? Esto significa que: las operaciones se realizan sobre los nombres de los objetos;
# esto es lo más importante a recordar: el nombre del objeto simple_function deja de indicar el objeto que
# representa nuestra simple_function () y desde ese momento indica el objeto devuelto por el decorador,
# el simple_decorator.

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def simple_hello():
    print("Hello from simple function!")


simple_hello()
