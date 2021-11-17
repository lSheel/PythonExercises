try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)
#UnicodeError tiene atributos que describen un error de codificación o decodificación.
# codificación: el nombre de la codificación que generó el error.
# motivo: una cadena que describe el error de códec específico.
# objeto: el objeto que el códec intentaba codificar o decodificar.
# inicio: el primer índice de datos no válidos en el objeto.
# end: el índice después de los últimos datos no válidos del objeto.