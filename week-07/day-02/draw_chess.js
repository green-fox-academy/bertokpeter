'use strict';
// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
let lineCount = 9;

for (let i = 1; i < lineCount+1; ++i) {
    let cell = ""
    let last = ""
    if (i%2 === 1) {
        cell = "% ";
        if (lineCount%2 === 1) {
            last = "%";
        }
    } else {
        cell = " %";
    }
    console.log(cell.repeat(Math.floor(lineCount/2)) + last);
}