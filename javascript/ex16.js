/*

16. Verifique se uma matriz é simétrica
Uma matriz quadrada é simétrica se for igual à sua transposta.

*/

let matriz = require("../matriz.json")

matriz = matriz.slice(0, matriz[0].length)

const rows = matriz.length
const cols = matriz[0].length

function ehSimetrica() {
    for (let j = 0; j < cols; j++){
        for (let i = 0; i < rows; i++){
            if (matriz[i][j] != matriz[j][i]){
                return false
            }
        }
    }
    return true
}

if (ehSimetrica()){
    console.log("A matriz é simétrica")
} else {
    console.log("A matriz não é simétrica")
}