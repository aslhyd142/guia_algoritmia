let nombres = ["Ana", "SOFIA", "Ana", "MARTIN", "Luis"];

let sinDuplicados = [];

for (let i = 0; i < nombres.length; i++) {

    if (!sinDuplicados.includes(nombres[i])) {
        sinDuplicados.push(nombres[i]);
    }
}

console.log(sinDuplicados);