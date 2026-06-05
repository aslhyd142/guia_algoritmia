function buscarEstudiante(lista, nombre) {
    return lista.find(est => est.nombre === nombre);
}