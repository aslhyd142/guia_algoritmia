let nombres = ["Ana", "Luis", "Carlos", "Maria"];

let buscar = "Carlos";

let encontrado = false;

for (let i = 0; i < nombres.length; i++) {

    if (nombres[i] == buscar) {
        console.log("Encontrado en posición", i);
        encontrado = true;
    }
}

if (encontrado == false) {
    console.log("No encontrado");
}