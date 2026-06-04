n=int(input("Ingrese la cantidad de notas: "))
estudiantes =(input("Ingrese el nombre del estudiante: "))
for i in range(n):
    nota = float(input("Ingrese la nota: "))
promedio = (nota) / n
if(promedio>=3.5):
        print(estudiantes+ " ha aprobado.")
else:
        print(estudiantes+ " ha reprobado.")
