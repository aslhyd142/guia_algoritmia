let promedios = [70, 95, 80, 60, 90];

for (let i = 0; i < promedios.length; i++) {

    let mayor = i;

    for (let j = i + 1; j < promedios.length; j++) {

        if (promedios[j] > promedios[mayor]) {
            mayor = j;
        }
    }

    let aux = promedios[i];
    promedios[i] = promedios[mayor];
    promedios[mayor] = aux;
}

console.log(promedios);