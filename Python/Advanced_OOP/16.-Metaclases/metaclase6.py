# Metaprogramación - otra metaclase
#Se crea la función greetings donde solo se manda a imprimir un saludo
def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')
#Nuestra clase meta
class My_Meta(type):
    #Pasamos nuestros argumentos
    def __new__(mcs, name, bases, dictionary):
        #Validamos si en el diccionario existe algun atributo en el diccionario que coincida con greetings
        #Si no es asi, se le agregara con el metodo anteriormente creado
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        #Llamamos el construtor de type
        obj = super().__new__(mcs, name, bases, dictionary)
        #Regresamos el objeto
        return obj
#Clase vacia
class My_Class1(metaclass=My_Meta):
    pass
#Clase con el metodo greetings
class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')
#Se crea el objeto, como __new__ tiene designado imprimir el greetings que se le asigno
myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()
