'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

let listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 8];

function numChecker(num_list) {
    let elements = [4,8,12,16];
    for (let i = 0; i < elements.length; i++) {
        if (num_list.indexOf(elements[i]) === -1) {
            return false;
        }
    }
    return true;
}

console.log(numChecker(listOfNumbers));