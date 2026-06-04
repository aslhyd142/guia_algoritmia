let n = 4;
let primo = true;

if (n < 2) {
    primo = false;
}

for (let i = 2; i < n; i++) {
    if (n % i == 0) {
        primo = false;
    }
}

if (primo) {
    console.log("Es primo");
} else {
    console.log("No es primo");
}