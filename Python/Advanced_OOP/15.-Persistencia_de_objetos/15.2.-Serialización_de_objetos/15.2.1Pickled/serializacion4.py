#A continuación, se muestra el mismo ejemplo sobre la definición de clases y el 'pickling de objetos:

import pickle

class Cucumber:

    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

cucu = Cucumber()

with open('cucumber.pckl', 'wb') as file_out:
    pickle.dump(cucu, file_out)

#No vemos errores, por lo que podríamos concluir que la clase y el objeto Cucumber se encurtieron correctamente
# y ahora podemos recuperarlos del archivo. De hecho, solo se conserva el objeto, pero no su definición,
# lo que nos permite determinar el diseño del atributo: Si ejecuta el código, recibe:

with open('cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())

#El remedio para los problemas anteriores es: el código que llama a las funciones load () o load () de pickle
# ya debería conocer la definición de función / clase.