'use strict';

let lineCount = 17;

// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (let i = 1; i < Math.floor((lineCount+1)/2+1); ++i) {
    console.log(" ".repeat(Math.floor((lineCount+1)/2-i)) + "*".repeat(i*2-1));
}
for (let i = 1; i < Math.floor(lineCount/2+1); ++i) {
    if (lineCount%2 !== 0) {
        console.log(" ".repeat(i) + "*".repeat(lineCount-i*2));
    } else {
        console.log(" ".repeat(i-1) + "*".repeat((lineCount+1)-i*2));
    }
} 
