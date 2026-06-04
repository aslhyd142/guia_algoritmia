let nombres = ["Ana", "Carlos", "Luis", "Maria"];

let buscar = "Luis";

let inicio = 0;
let fin = nombres.length - 1;

let encontrado = false;

while (inicio <= fin) {

    let medio = Math.floor((inicio + fin) / 2);

    if (nombres[medio] == buscar) {
        console.log("Encontrado en posición", medio);
        encontrado = true;
        break;
    }

    if (nombres[medio] < buscar) {
        inicio = medio + 1;
    } else {
        fin = medio - 1;
    }
}

if (encontrado == false) {
    console.log("No encontrado");
}