'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

let girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
let boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
let order = [];

for (let i = 0; i < Math.max(girls.length, boys.length); i++) {
    if (girls.length > i) {
        order.push(girls[i]);
    }
    if (boys.length > i) {
        order.push(boys[i]);
    }
}

console.log(order);