from datetime import datetime

#Estamos creando una clase que va heredar a dict
class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        #Constructor de la clase padre
        super().__init__(*args, **kwargs)
        #Se crea una lista
        self.log = list()
        #Mensajes a mostrar
        self.log_timestamp('MonitoredDict created')
    #Se sobreescribe el metodo __getitem_ de dict
    def __getitem__(self, key):
        #Se llama al metodo getitem de la clase padre, no la que creamos
        val = super().__getitem__(key)
        self.log_timestamp('value for key [{}] retrieved'.format(key))
        #Regresa el item que solicitamos del metodo
        return val
    #Lo mismo que el metodo get pero ahora sera agregar/poner el valor que se le paso
    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp('value for key [{}] set'.format(key))
    #Metodo el cual es el que estamos utilizando para mandar el mensaje de cuando se manda el mensaje
    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append('{} {}'.format(timestampStr, message))

#Se crea el objeto con 0 items en el diccionario
kk = MonitoredDict()
#Empezamos a agregar valores a la lista
kk[10] = 15
kk[20] = 5

print('Element kk[10]:', kk[10])
print('Whole dictionary:', kk)
print('Our log book:\n')
#Lo que hace join es agregar a la impresion la lista log del objeto creado si necesidad de hacer un bucle de impresion
print('\n'.join(kk.log))
