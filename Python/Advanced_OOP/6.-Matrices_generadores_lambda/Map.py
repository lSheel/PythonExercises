# Map: de la funcion map necesita dos argumentos, el metodo lambda y la lista, el cual generara su propio
# lista del resultado generado por el metodo que es 2 a la x donde x es cada iteracion de la lista
lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
    print(x, end=' ')

