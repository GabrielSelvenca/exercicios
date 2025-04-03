/* 

13.Diagonal principal
Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal principal.

*/

let matriz = require("../matriz.json")

matriz = matriz.slice(-matriz[0].length)

matriz.forEach((row, i) => {
    console.log(row[i])
})