'use strict';
// - Create a variable named `am` and assign the value `kuty` to it
// - Write a function called `appendA` that gets a string as an input
//   and appends an 'a' character to its end
// - Print the result of `appendA(am)` to the console
let am = 'kuty';
console.log(appendA(am));

function appendA(text) {
    let newText = text + 'a'
    return newText
}