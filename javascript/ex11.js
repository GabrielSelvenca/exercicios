/*

11. Soma de cada linha
Dada uma matriz, calcule a soma dos elementos de cada linha e exiba os
resultados.

*/

const matriz = require("../matriz.json")

soma = 0

matriz.forEach((row, i) => {
    row.forEach(num => {
        soma += num
    })
    console.log(`Soma da linha ${i+1}: ${soma}`)
    soma = 0
})