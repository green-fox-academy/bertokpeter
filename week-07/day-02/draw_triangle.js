'use strict';

let lineCount = 10;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for (let i = 1; i < lineCount+1; ++i) {
    console.log("*".repeat(i));
}