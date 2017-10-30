class Animal {

    constructor() {
        this.hunger = 5;
        this.thirst = 5;
    }
    
    eat() {
        this.hunger -= 1;
    }
    
    drink() {
        this.thirst -= 1;
    }
    
    play() {
        this.thirst += 1;
        this.hunger += 1;
    }
}

class Farm {

    constructor(slots) {
        this.slots = slots;
        this.animals = [];
        for (let i = 0; i < this.slots; i++){
            this.animals.push(new Animal());
        }
    }

    breed() {
        if (this.animals.length < this.slots) {
            this.animals.push(new Animal());
        }
    }

    slaughter() {
        let hungerList = this.animals.map(function(e){
            return e.hunger; 
        });
        let min = Math.min.apply(Math, hungerList);
        this.animals.splice(hungerList.indexOf(min), 1);
    }

    report() {
        let state = '';
        if (this.animals.length === 0) {
            state = ' bankrupt';
        } else if (this.animals.length < this.slots) {
            state = ' okay';
        } else {
           state = ' full';
        }
        console.log('We have ' + this.animals.length + ' living animals. We are' + state);
    }

    progress() {
        this.animals.forEach(function(e,i){
            let randNumbers = [];
            for (let i = 0; i < 3; i++){
                randNumbers.push(Math.random());
            }
            if (randNumbers[0] >= 0.5) {
                e.eat();
            } 
            if (randNumbers[1] >= 0.5) {
                e.drink();
            }
            if (randNumbers[2] >= 0.5) {
                e.play();
            }
        });
        this.breed();
        this.slaughter();
        this.report();
    }
}
// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 25 Animal objects

const button = document.querySelector('button');

// Add a click event to the button and call 'progress'

button.addEventListener('click', SheepFarm.progress.bind(SheepFarm));

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full