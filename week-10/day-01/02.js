'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

class Rectangles {
    constructor(sideA, sideB){
        this.sideA = sideA;
        this.sideB = sideB;
    }
    
    getArea(){
        return this.sideA*this.sideB
    }

    getCircumference(){
        return this.sideA*2+this.sideB*2
    }
}

const brick = new Rectangles(5, 9);

console.log(brick.getArea())
console.log(brick.getCircumference())