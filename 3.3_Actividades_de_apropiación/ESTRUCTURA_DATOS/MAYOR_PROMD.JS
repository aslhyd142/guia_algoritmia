let nombres = ["Ana", "Luis", "Carlos"];
let promedios = [80, 95, 70];

let mejor = nombres[0];
let mayor = promedios[0];

for (let i = 1; i < promedios.length; i++) {

    if (promedios[i] > mayor) {
        mayor = promedios[i];
        mejor = nombres[i];
    }
}

console.log("Mejor estudiante:", mejor);
console.log("Promedio:", mayor);