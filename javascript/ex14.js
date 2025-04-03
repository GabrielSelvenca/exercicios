/*

14.Diagonal secundária
Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal
secundária.

*/

let matriz = require("../matriz.json")

matriz = matriz.slice(-matriz[0].length)

n = matriz.length

matriz.forEach((_, i) => {
    console.log(matriz[i][n - 1 - i])
})