"use strict";
let num = [];
let maior = 0;
for (let index = 0; index < 20; index++) {
    let a = Math.random() * 99;
    let n = parseInt(a.toString());
    num.push(n);
    if (num[index] > maior)
        maior = num[index];
}
console.log(num);
console.log(maior);
