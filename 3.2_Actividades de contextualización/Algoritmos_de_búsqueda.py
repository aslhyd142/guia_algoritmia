def buscar_estudiante(lista, nombre):
    for est in lista:
        if est["nombre"] == nombre:
            return est
    return None