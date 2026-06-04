cantidad = int(input("Cantidad de estudiantes: "))

nombres = []
promedios = []

for i in range(cantidad):

    nombre = input("Nombre: ")

    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3
    print("Promedio de " + nombre + ": " + str(promedio))
if (nota1 < nota2 and nota1 < nota3) and promedio >= 3:
    print("El orden desde los promedios es: " + nombres + " Aprobado")
elif (nota2 < nota1 and nota2 < nota3) and promedio < 3:
    print(nombre + " Reprobado")
elif(nota3 < nota1 and nota3 < nota2) and promedio < 3:
    print(nombre + " Reprobado")