"use strict";
const nota1 = 7;
const nota2 = 8;
const nota3 = 5;
const media = (nota1 + nota2 + nota3) / 3;
console.log(`A média das notas é ${media}`);
if (media >= 7) {
    console.log("Aprovado");
}
else if (media >= 5) {
    console.log("Recuperação");
}
else if (media < 5) {
    console.log("Reprovado");
}
