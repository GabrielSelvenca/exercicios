/*

9. Soma de todos os elementos da matriz
Dada uma matriz N x M, retorne a soma de todos os seus elementos.

*/

const matriz = require("../matriz.json")

let soma = 0

matriz.forEach(row => {
    row.forEach(num => {
        soma+=num
    })
})

console.log(`Soma: ${soma}`)