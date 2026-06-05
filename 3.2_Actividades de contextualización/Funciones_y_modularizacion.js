function calcularPromedio(notas) {
    return notas.reduce((a, b) => a + b, 0) / notas.length;
}

console.log(calcularPromedio([4.0, 3.5, 5.0]));