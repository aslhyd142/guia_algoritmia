let nombres = ["Ana", "Luis", "Carlos"];

let nota1 = [80, 90, 70];
let nota2 = [90, 95, 80];
let nota3 = [85, 100, 75];

let promedios = [];

for (let i = 0; i < nombres.length; i++) {

    let promedio = (nota1[i] + nota2[i] + nota3[i]) / 3;

    promedios.push(promedio);
}

for (let i = 0; i < promedios.length; i++) {

    for (let j = 0; j < promedios.length - 1; j++) {

        if (promedios[j] < promedios[j + 1]) {

            let aux = promedios[j];
            promedios[j] = promedios[j + 1];
            promedios[j + 1] = aux;

        let auxNombre = nombres[j];
          nombres[j] = nombres[j + 1];
          nombres[j + 1] = auxNombre;
        }
    }
}

console.log("Lista ordenada");

for (let i = 0; i < nombres.length; i++) {
    console.log(nombres[i], promedios[i]);
}

let buscar = "Luis";

for (let i = 0; i < nombres.length; i++) {

    if (nombres[i] == buscar) {
        console.log("Promedio:", promedios[i]);
    }
}

console.log("Mejor estudiante:", nombres[0]);
console.log("Promedio:", promedios[0]);