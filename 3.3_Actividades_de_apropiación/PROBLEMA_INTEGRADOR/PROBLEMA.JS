let cantidad = 3;

let nombres = ["Ana", "Juan", "Pedro"];
let promedios = [4.3, 4.8, 3.5];

// Búsqueda por nombre

let buscar = "Juan";

for (let i = 0; i < cantidad; i++) {
    if (nombres[i] == buscar) {
        console.log("Nombre: " + nombres[i]);
        console.log("Promedio: " + promedios[i]);
    }
}

// Mejor estudiante

let mayor = promedios[0];
let mejor = nombres[0];

for (let i = 0; i < cantidad; i++) {
    if (promedios[i] > mayor) {
        mayor = promedios[i];
        mejor = nombres[i];
    }
}

console.log("Mejor estudiante: " + mejor);
console.log("Promedio: " + mayor);