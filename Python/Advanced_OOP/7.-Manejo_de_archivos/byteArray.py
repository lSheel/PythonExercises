####BYTEARRAY####
#¿Qué es un bytearray?
#Antes de comenzar a hablar sobre archivos binarios, tenemos que informarte sobre una de las clases
#especializadas que Python usa para almacenar datos amorfos.

#Los datos amorfos son datos que no tienen forma específica - son solo una serie de bytes.

#Esto no significa que estos bytes no puedan tener su propio significado o que no puedan representar ningún
#objeto útil, por ejemplo, gráficos de mapa de bits.


#Existe una limitación importante - no debes establecer ningún elemento del arreglo de bytes con un valor
#que no sea un entero (violar esta regla causará una excepción TypeError) y tampoco está permitido asignar
#un valor fuera del rango de 0 a 255 (a menos que quieras provocar una excepción ValueError).

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
    print(b)