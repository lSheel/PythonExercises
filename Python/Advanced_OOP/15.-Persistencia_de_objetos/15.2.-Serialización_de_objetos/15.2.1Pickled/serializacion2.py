#Los objetos serializados podrían persistir en una base de datos o enviarse a través de una red.
# Esto implica otras dos funciones correspondientes a las funciones pickle.dumps () y pickle.loads ():

#pickle.dumps (object_to_be_pickled) - espera un objeto inicial, devuelve un objeto byte. Este objeto de byte debe
#       pasarse a una base de datos o controlador de red para conservar los datos;
#pickle.loads (bytes_object) - espera el objeto bytes, devuelve el objeto inicial.

import pickle

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# Pasa 'bytes' al controlador apropiado

# Por lo tanto, cuando recibe un objeto de bytes de un controlador apropiado, puede deserializarlo
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)
