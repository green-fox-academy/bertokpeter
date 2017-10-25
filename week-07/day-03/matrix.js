'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

let rows = 4;
let matrix = [];

for (let i = 0; i < rows; ++i) {
    let row = [];
    for (let j = 0; j < rows; ++j) {
        row.push(0);
    }
    row[rows-i-1] = 1;
    matrix.push(row);
    console.log(matrix[i]);
}