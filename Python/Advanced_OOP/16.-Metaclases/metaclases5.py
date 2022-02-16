#Es importante recordar que las metaclases son clases de las que se crean instancias para obtener clases.
# El primer paso es definir una metaclase que se deriva del tipo type y arma la clase con un 'custom_attribute',
# de la siguiente manera:

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj

class My_Object(metaclass=My_Meta):
    pass

print(My_Object.__dict__)

#Preste atención al hecho de que:
# La clase My_Meta se deriva de type. Esto hace que nuestra clase sea una metaclase;
# Nuestro propio método __new__ ha sido definido. Su función es llamar al método __new__ de la clase padre para
# crear una nueva clase;
# __new__ usa 'mcs' para referirse a la clase; es solo una convención;
# Además, se crea un atributo de clase; se devuelve la clase.