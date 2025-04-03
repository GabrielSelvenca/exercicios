/*

12. Soma de cada coluna
Dada uma matriz, calcule a soma dos elementos de cada coluna e exiba os
resultados.

*/

const matriz = require("../matriz.json")

let soma = 0
let i = 0

for (let i = 0; i < matriz[i].length; i++) {
    matriz.forEach(row => {
        soma+=row[i]
    })
    console.log(`Soma da coluna ${i+1}: ${soma}`)
    soma = 0
}