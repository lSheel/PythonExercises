##############Lectura y escritura de bytearrays########################3
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    hola = bytearray(bf.read())
    for b in hola:
        print(hola(b), end = "")
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))