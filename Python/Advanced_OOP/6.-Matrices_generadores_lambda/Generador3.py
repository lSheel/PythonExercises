# Yield convierte una funcion en un generador
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2


for v in potenciasDe2(8):
    print(v)

listaUno = []

for ex in range(6):
    listaUno.append(10 ** ex)

listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)
