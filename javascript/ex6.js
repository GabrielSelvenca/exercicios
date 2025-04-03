/*

6. Inverta um array
Dado um array, retorne um novo array com os elementos invertidos.

*/

const array = require("../array.json")

let novoArray = []

for (let i = 0; i < array.length; i++) {
    const num = array[(array.length - 1) - i];
    novoArray.push(num)
}

console.log("Novo array invertido: " + novoArray + "\n\n\nTamanho do original: " + array.length + "\nTamanho do novo: " + novoArray.length)
