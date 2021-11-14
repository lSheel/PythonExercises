class Car:
    #El constructor que pide un parametro
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    #El metodo class
    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        #Lo que va hacer la sig es crear un objeto, para eso se usa cls para referise a la clase y le pasamos el
        # parametro que necesitamos que es vin
        _car = cls(vin)
        #Le asignamos un valor a brand que es un atributo de car
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)
