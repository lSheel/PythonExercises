temps = [[0.0 for h in range(24)] for d in range(31)]
#
# la matriz se actualiza mágicamente aquí
#

mas_alta = -100.0

for day in temps:
    print(day)
    for temp in day:
        print(temp)
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)
