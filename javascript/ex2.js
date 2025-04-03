/*

2. Encontre o menor número
Dado um array, retorne o menor número presente nele.

*/

const array = require("../array.json")

let menor = array[0]

array.forEach(num => {
    if (num < menor) menor = num
})

console.log("Menor número: " + menor)