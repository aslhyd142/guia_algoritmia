nombres = ["Ana", "Carlos", "Luis", "Maria"]

buscar = input("Nombre a buscar: ")

inicio = 0
fin = len(nombres) - 1

encontrado = False

while inicio <= fin:

    medio = (inicio + fin) // 2

    if nombres[medio] == buscar:
        encontrado = True
        print("Encontrado en posición", medio)
        break

    elif nombres[medio] < buscar:
        inicio = medio + 1

    else:
        fin = medio - 1

if encontrado == False:
    print("No encontrado")