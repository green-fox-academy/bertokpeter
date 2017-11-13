'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(voice){
    this.voice = voice;
}

const cat = new Animal('meow');

Animal.prototype.say = function(){
    console.log(this.voice);
}
cat.say();