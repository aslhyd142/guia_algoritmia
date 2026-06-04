let promedios = [70, 95, 80, 60, 90];

for (let i = 0; i < promedios.length; i++) {

    for (let j = 0; j < promedios.length - 1; j++) {

        if (promedios[j] < promedios[j + 1]) {

            let aux = promedios[j];
            promedios[j] = promedios[j + 1];
            promedios[j + 1] = aux;
        }
    }
}

console.log(promedios);