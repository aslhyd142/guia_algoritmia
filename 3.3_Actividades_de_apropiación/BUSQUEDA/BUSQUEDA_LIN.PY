nombres = ["Ana", "Luis", "Carlos", "María"]

buscar = input("Nombre a buscar: ")

posicion = -1

for i in range(len(nombres)):
    if nombres[i] == buscar:
        posicion = i

if posicion != -1:
    print("Encontrado en posición", posicion)
else:
    print("No encontrado")