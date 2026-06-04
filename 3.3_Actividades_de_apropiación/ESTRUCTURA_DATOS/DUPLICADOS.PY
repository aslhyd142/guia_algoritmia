nombres = ["Ana", "Luis", "Ana", "Carlos", "Luis"]

sin_duplicados = []

for nombre in nombres:
    if nombre not in sin_duplicados:
        sin_duplicados.append(nombre)

print(sin_duplicados)