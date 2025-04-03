/*

3. Calcule a soma dos elementos
Dado um array, calcule a soma de todos os seus elementos.

*/

const array = require("../array.json")

let soma = 0

array.forEach(num => {
    soma += num
})

console.log("Soma do array: " + soma)