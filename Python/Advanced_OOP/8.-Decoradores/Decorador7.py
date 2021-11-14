def object_counter(class_):
    #Se crea un metodo que va a copiar a __getattribute__
    class_.__getattr__orig = class_.__getattribute__

    #Se crea un nuevo metodo que tomara el papel de __getattribute___ el cual tomara el nombre del atributo
    def new_getattr(self, name):
        #Puede ser un poco confuso, pero como se toma el objeto, digamos que el valores del atributo va a ser el
        #nombre del atributo por como se llama
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        #retorna el metodo original para que, pueda regresar el valor de atributo
        return class_.__getattr__orig(self, name)
    #Se define que __getattribute__ pasa a ser new_getattr
    class_.__getattribute__ = new_getattr
    #Se devuelve el objeto decorado
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)
