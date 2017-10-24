'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let a = 3.5;
let b = 4.5;
let c = 5.5;

console.log("Surface Area: " + (a*b*2 + b*c*2 + a*c*2));
console.log("Volume: " + a*b*c);