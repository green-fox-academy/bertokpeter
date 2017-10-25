'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result
function summing(number) {
    let summa = 0
    for (let i = 1; i < number+1; ++i) {
        summa += i
    }    
    return summa
}

console.log(summing(6));