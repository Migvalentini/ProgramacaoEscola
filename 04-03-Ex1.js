"use strict";
function fatorial(numero) {
    let soma = 1;
    for (let index = 1; index <= numero; index++) {
        soma = soma * index;
    }
    console.log(soma);
}
for (let index = 0; index < 10; index++) {
    fatorial(index);
}
