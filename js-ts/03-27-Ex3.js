"use strict";
function maior_elemento(array) {
    let maior = array[0];
    array.forEach(element => {
        if (element > maior) {
            maior = element;
        }
    });
    return maior;
}
console.log(`O maior elemento do vetor é: ${maior_elemento([-32, -9, -50])}`);
