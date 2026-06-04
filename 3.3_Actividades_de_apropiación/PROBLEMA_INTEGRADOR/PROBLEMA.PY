cantidad = int(input("Cantidad de estudiantes: "))

nombres = []
promedios = []

for i in range(cantidad):

    nombre = input("Nombre: ")

    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    nombres.append(nombre)
    promedios.append(promedio)

# Ordenamiento burbuja
for i in range(len(promedios)):
    for j in range(len(promedios) - 1):

        if promedios[j] < promedios[j + 1]:

            aux = promedios[j]
            promedios[j] = promedios[j + 1]
            promedios[j + 1] = aux

            aux2 = nombres[j]
            nombres[j] = nombres[j + 1]
            nombres[j + 1] = aux2

print("\nLISTA ORDENADA")

for i in range(len(nombres)):
    print(nombres[i], "-", round(promedios[i], 2))

buscar = input("\nNombre a buscar: ")

encontrado = False

for i in range(len(nombres)):

    if nombres[i].lower() == buscar.lower():

        print("Promedio:", round(promedios[i], 2))
        encontrado = True

if encontrado == False:
    print("No encontrado")

print("\nMejor estudiante:")
print(nombres[0], "-", round(promedios[0], 2))