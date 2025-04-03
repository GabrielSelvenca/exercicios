/*

4. Calcule a média dos elementos
Dado um array de números, retorne a média dos valores.

*/

const array = require("../array.json")

let soma = 0

array.forEach(num => {
    soma += num
})

media = soma / array.length

console.log("Media da array: " + media)