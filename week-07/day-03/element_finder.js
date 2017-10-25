'use strict';

// Check if the array contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

let numbers = [1,2,3,4,5,6,8];

let find = numbers.some(function(e) {
    return e === 7;
});

let finder1 = function (){
    if (find) {
        console.log("Hooray");
    } else {
        console.log("Nooooo");
    }
};

finder1()

let finder2 = function (){
    if (numbers.indexOf(7) !== -1) {
        console.log("Hooray");
    } else {
        console.log("Nooooo");
    }
};

finder2()