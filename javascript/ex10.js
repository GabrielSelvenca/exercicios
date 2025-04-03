/*

10. Encontre o maior elemento de uma matriz
Dada uma matriz N x M, encontre o maior número presente nela

*/

const matriz = require("../matriz.json")

let maior = 0

matriz.forEach(row => {
    row.forEach(num => {
        if (num > maior) maior = num
    })
})

console.log("Maior número da lista: " + maior)