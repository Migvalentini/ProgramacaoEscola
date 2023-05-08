"use strict";
const calculoJuros = (principal = 100, meses = 5, taxa = 3) => {
    let resultado = (principal * meses * taxa) / 100;
    return resultado;
};
console.log(calculoJuros(100, 5, 3));
const fat = (n) => {
    if (n === 0) {
        return 1;
    }
    for (let i = n - 1; i >= 1; i--) {
        n *= i;
    }
    return n;
};
const n = 5;
const factorial = fat(n);
console.log(`O fatorial de ${n} é ${factorial}`);
