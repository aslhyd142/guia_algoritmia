cantidad = int(input("Cantidad de estudiantes: "))

nombres = [0] * cantidad
promedios = [0] * cantidad

for i in range(cantidad):

    nombres[i] = input("Nombre: ")

    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    promedios[i] = (nota1 + nota2 + nota3) / 3

    print("Promedio de", nombres[i], ":", promedios[i])

# Búsqueda por nombre

buscar = input("Ingrese el nombre a buscar: ")

for i in range(cantidad):
    if nombres[i] == buscar:
        print("Nombre:", nombres[i])
        print("Promedio:", promedios[i])

# Mejor estudiante

mayor = promedios[0]
mejor = nombres[0]

for i in range(cantidad):
    if promedios[i] > mayor:
        mayor = promedios[i]
        mejor = nombres[i]

print("Mejor estudiante:", mejor)
print("Promedio:", mayor)