let number: number[] = []

for (let index = 0; index < 10; index++) {
    let a = Math.random() * 99
    let n = parseInt(a.toString())
    num.push(n)
}
console.log(num)

function media_numeros(array: number[]) {
    let soma = 0
    for (let index = 0; index < array.length; index++) {
        soma += array[index]
    }
    console.log(soma / array.length)
}

media_numeros(num)