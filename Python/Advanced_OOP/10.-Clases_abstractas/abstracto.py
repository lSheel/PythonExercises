#Para poder usar las clases abstractas debemos importar abc
import abc

#En la clase abstracta, debemos pasar como parametro abc.ABC (significa Abstract Base Classes (ABC))
class BluePrint(abc.ABC):
    #Si queremos hacer un metodo abstracto lo debemos decorar con @abc.abstractmethod
    @abc.abstractmethod
    def hello(self):
        pass

#En esta clase estamos heredando la clase abstracta
class GreenField(BluePrint):
    #Como se puede ver, se esta sobreescribiendo el metodo hello asignandole su propio funcionamiento
    def hello(self):
        print('Welcome to Green Field!')

#Aqui pasa lo mismo que GreenField, le estamos herendando pero nos va a mandar el siguiente error
         ###Can't instantiate abstract class RedField with abstract method hello###
#Esto por que no estamos estanciando el metodo hello, es necesario sobreescribirla de lo contrario no tendria sentido
#hacer la herencia
class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()

rf = RedField()
