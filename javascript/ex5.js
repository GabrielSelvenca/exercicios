/*

5. Conte os números pares e ímpares
Dado um array de números inteiros, conte quantos são pares e quantos são
ímpares.

*/

const array = require("../array.json")

let pares = 0
let impares = 0

array.forEach(num => {
    if (num%2==0) {pares++} else impares++
})

console.log("Pares: " + pares + "\n\nImpares: " + impares)