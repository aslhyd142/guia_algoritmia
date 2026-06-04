promedios = [70, 95, 80, 60, 90]

for i in range(len(promedios)):

    mayor = i

    for j in range(i + 1, len(promedios)):

        if promedios[j] > promedios[mayor]:
            mayor = j

    aux = promedios[i]
    promedios[i] = promedios[mayor]
    promedios[mayor] = aux

print(promedios)