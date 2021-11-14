temps = [[0.0 for h in range(24)] for d in range (31)]

suma = 0.0
for day in temps:
    for i in range(24):
        day[i] = 2*i
    suma += day[11]
print(temps)
promedio = suma / 31

print("Temperatura promedio al mediodía:", promedio)


lista = [6 for f in range(10)]
print(lista)