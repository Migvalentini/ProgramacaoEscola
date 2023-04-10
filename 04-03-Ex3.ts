function fibonacci(termo: number) {
    let penultimo = 0
    let ultimo = 1
    let numero

    if(termo <= 2) {
        numero = termo - 1
    } else {
        for (let index = 3; index <= termo; index++) {
            numero = ultimo + penultimo
            penultimo = ultimo
            ultimo = numero
            //console.log(numero, ultimo, penultimo)
    }
    }
    return numero
}

console.log(fibonacci(8))
console.log(fibonacci(12))