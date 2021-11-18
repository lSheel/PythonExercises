#El siguiente código demuestra la situación del decapado de la definición de

import pickle

def f1():
    print('Hello from the jar!')

with open('function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)

#Si eliminamos No vemos errores, por lo que podríamos concluir que f1 () fue 'pickled' correctamente y ahora podemos recuperarlo
# del archivo. Ejecute el código en el editor y vea qué sucede. Desafortunadamente, el resultado prueba que no se
# mantuvo ningún código:

with open('function.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
data()
