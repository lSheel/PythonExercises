#¿Qué es esa 'identidad' de objeto?
# ¿Por qué el valor del objeto y la etiqueta no son suficientes?
# La función incorporada id () devuelve la 'identidad' de un objeto.
# Este es un número entero que se garantiza que será único y constante para este objeto durante su vida útil.
# Dos objetos con vidas útiles que no se superponen pueden tener el mismo valor de id ().

#####NOTA#####
#Detalle de implementación de CPython:
# esta es la dirección del objeto en la memoria. No lo trate como una dirección de memoria absoluta.

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

#Cuando tiene dos variables que se refieren al mismo objeto,
# los valores de retorno de la función id () deben ser los mismos.

a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
