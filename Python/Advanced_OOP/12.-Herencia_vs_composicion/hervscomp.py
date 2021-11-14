class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number

#Se le herada la clase Base_Computer
class Personal_Computer(Base_Computer):
    #Aqui se usara la composicion, la conexion se podria decir "es parte de la computadora"
    #entonces sin problemas podemos usar la composicion (se pasa como parametro)
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')


class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))

#Se le va a heredar la clase coneccion ya que tenmos varias conexiones entonces seria un "es una conexion..." o
#"viene de"
class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()

#Otra clase que se hereda
class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()

#Otra clase que se hereda
class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

# Se inicia una conexcion dial up
#Se pasa el tipo de conexion que vamos a usar
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# Mejoramos la conexion y ahora haremos la conexion ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# Finalmente nos hemos podido actualizar a ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()