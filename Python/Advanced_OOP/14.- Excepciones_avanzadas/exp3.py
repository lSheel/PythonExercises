#¿Qué son las excepciones encadenadas?
# Python 3 introdujo una característica muy interesante llamada 'Encadenamiento de excepciones' para tratar de manera
# efectiva las excepciones. Imagine una situación en la que ya está manejando una excepción y su código desencadena
# una excepción adicional. ¿Debería su código perder la información sobre la excepción anterior?
# Por supuesto no. Por lo tanto, la información debe estar disponible para el código que sigue al código erróneo.
# Este concepto de encadenamiento introduce dos atributos de instancias de excepción:
# el atributo __context__, que es inherente a las excepciones encadenadas implícitamente;
#

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)
