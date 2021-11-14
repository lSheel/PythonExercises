# Cierres
# Los cierres de alguna manera se podria decir que son funciones (interiores) dentro de otra funcion (exterior)
# que utilizan sus variables sin necesisad de pedir parametro.
# cierres es una técnica que permite almacenar valores a pesar de que el contexto
# en el que se crearon ya no exist (en este caso la funcion exterior).

# Fucion con cierre
def exterior(par):
    loc = par

    def interior():
        return loc

    return interior


var = 1
fun = exterior(var)
print(fun())


# Funcion con el mismo algoritmo

def exterior(par):
    loc = par
    return interior


def interior(hola):
    hola = exterior.loc
    return hola


ejem = 1
func = exterior(ejem)
print(fun())


# Otra funcion creada con cierres
def crearcierre(par):
    loc = par

    def potencia(p):
        return p ** loc

    return potencia


fsqr = crearcierre(2)
fcub = crearcierre(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))
