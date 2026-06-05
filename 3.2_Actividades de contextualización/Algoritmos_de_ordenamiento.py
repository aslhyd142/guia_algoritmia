def ordenar_por_promedio(estudiantes):
    return sorted(estudiantes, key=lambda est: sum(est["notas"]) / len(est["notas"]), reverse=True)