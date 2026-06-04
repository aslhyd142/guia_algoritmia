promedios = [70, 95, 80, 60, 90]

for i in range(len(promedios)):
    for j in range(len(promedios) - 1):

        if promedios[j] < promedios[j + 1]:

            aux = promedios[j]
            promedios[j] = promedios[j + 1]
            promedios[j + 1] = aux

print(promedios)