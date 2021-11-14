from random import seed, randint

# seed es el generador de nuemros aleatorios
seed()
# Aqui ex una lista generada con numeros aletorios del -10 al 10
data = [randint(-10, 10) for x in range(5)]
# Aqui es donde la var filtered creara una lista donde la funcion filter necesita dos argumentos, la funcion lambda
# y la lista donde se especifica que solo sera True si el numero es la lista data es mayor a 0 y no tiene residuo
# Al momento de dividir, al imprimir las listas, filtered solo imprime los numeros que cumplen con lo requisitos
# especificados en el funcion lambda
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)
