#Usar shelve es bastante fácil e intuitivo. Primero, importemos el módulo apropiado y creemos un objeto
# que represente una base de datos basada en archivos:

# import shelve
# my_shelve = shelve.open('first_shelve.shlv', flag='w')

#El significado del parámetro de bandera opcional:

#Value	Meaning
#'r' 	Abre la base de datos existente para solo lectura
#'w' 	Abre la base de datos existente para lectura y escritura
#'c' 	Abre la base de datos existente para lectura y escritura, La crea si no existe (Es el valor por default)
#'n'   Siempre crea una base de datos nueva y vacia, para lectura y escritura

import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
#Ahora nuestro objeto de estantería está listo para la acción, así que insertemos algunos elementos y
# cierre el objeto de estantería.
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

#Ahora abramos el archivo shelve para demostrar el acceso directo a los elementos
# (contrario al acceso secuencial a los elementos cuando usamos pickles).

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()