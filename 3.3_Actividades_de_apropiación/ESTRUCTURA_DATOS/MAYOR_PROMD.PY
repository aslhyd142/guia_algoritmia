cantidad = int(input("Cantidad de estudiantes: "))

mejor_nombre = ""
mejor_promedio = 0

for i in range(cantidad):

    nombre = input("Nombre: ")

    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_nombre = nombre

print("Mejor estudiante:", mejor_nombre)
print("Promedio:", mejor_promedio)