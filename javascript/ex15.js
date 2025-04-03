/*

15. Transposta de uma matriz
Dada uma matriz N x M, gere sua transposta (troque linhas por colunas).

*/

const matriz = require("../matriz.json")

const rows = matriz.length
const cols = matriz[0].length

let novaMatriz = []

for (let j = 0; j < cols; j++) {
    let newRow = []
    for (let i = 0; i < rows; i++) {
        newRow.push(matriz[i][j])
    }
    novaMatriz.push(newRow)
}

console.log("Nova matriz: \n\n")

console.log(novaMatriz)

console.log(`\n\n\nComparando tamanhos:\n\n\nMatriz Original:\n\nLinhas: ${rows}\nColunas: ${cols}\n\nNova:\n\nLinhas: ${novaMatriz.length}\nColunas: ${novaMatriz[0].length}\n\n`)