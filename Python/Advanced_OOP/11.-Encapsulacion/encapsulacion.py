#La encapsulación se usa para ocultar los atributos dentro de una clase como en una cápsula,
#evitando el acceso directo a ellos por parte de personas no autorizadas. Los métodos de acceso público se
#proporcionan en la clase para acceder a los valores, y otros objetos llaman a esos métodos para recuperar y
#modificar los valores dentro del objeto. Esta puede ser una forma de hacer cumplir una cierta cantidad de privacidad para los atributos.

#Python le permite controlar el acceso a los atributos con la función property () incorporada y el decorador
# correspondiente @property.

#@ tank.setter (): designa el método llamado para establecer el valor del atributo encapsulado;
# @ tank.deleter (): designa el método llamado cuando otro código desea eliminar el atributo encapsulado.
class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0
    #getter de level
    @property
    def level(self):
        return self.__level
    #setter de level
    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')
    #deleter de level
    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None


# el objeto our_tank se le asignan 20 unidades
our_tank = Tank(20)

# our_tank's se le asigna un nivel de 10 unidades
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# Se le agregan 3 unidades a level
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# Se intentara asignar 21 unidades a level
# No deberia dejar porque la capacidad maxima que le asignamos es 20 unidades
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# Un caso similar pero ahora se le intentara agregar 15 unidades
# Igual deberia mandar error porque el maximo es 20 unidades
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# Ahora se intentara asginar unidades negativas
# Igual lo deberia de rechazar
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

#Volvemos a imprimir el resultado
print('Current liquid level:', our_tank.level)

#Se borra el liquido
del our_tank.level
