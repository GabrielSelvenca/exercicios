/*

Encontre o maior número
Dado um array, retorne o maior número presente nele.

*/

const array = require("../array.json")

let maior = array[0]

array.forEach(num => {
    if (maior < num) maior = num
})

console.log("Maior número: " + maior)