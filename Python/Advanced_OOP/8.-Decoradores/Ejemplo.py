def object_counter(ejem):
    ejem.__getattr_si = ejem.__getattribute__

    def new_getattr(self, name):
        #si es va
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return ejem.__getattr_si(self, name)

    ejem.__getattribute__ = new_getattr

    return ejem


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)
