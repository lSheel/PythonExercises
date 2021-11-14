####write#####
from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i + 1) + "\n")
    fo.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

####Otro ejemplo pero escribiendo letra por letra####
from os import strerror

try:
    fo = open('newtext.txt', 'wt')  # un nuevo archivo (newtext.txt) es creado
    for i in range(10):
        s = "línea #" + str(i + 1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
