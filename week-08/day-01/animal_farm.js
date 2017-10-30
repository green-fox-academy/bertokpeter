// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 25 Animal objects

const button = document.querySelector('button');

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full

class Animal {

    constructor() {
        this.hunger = 5;
        this.thirst = 5;
    }

    eat () {
        this.hunger -= 1;
    }

    drink () {
        this.thirst -= 1;
    }

    play () {
        this.thirst += 1;
        this.hunger += 1;
    }
}