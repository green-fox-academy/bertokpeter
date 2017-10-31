'use strict';
class ElevatorModel {
    constructor(maxfloor, maxpeople){
        this.maxfloor = maxfloor;
        this.maxpeople = maxpeople;
        this.position = 10;
        this.people = 0;
    }

    checkLimits(action){
        if (action === 'add') {
            return this.people < this.maxpeople;
        } else if (action === 'remove') {
            return this.people > 0;
        } else if (action === 'up') {
            return this.position > 1;
        } else if (action === 'down') {
            return this.position < this.maxfloor;
        }
    }

    addPeople() {
        if (this.checkLimits('add')) {
            this.people += 1;
        }
    }

    removePeople() {
        if (this.checkLimits('remove')) {
            this.people -= 1;
        }
    }

    elevatorUp() {
        if (this.checkLimits('up')){
            this.position -= 1;
        }
    }

    elevatorDown() {
        if (this.checkLimits('down')) {
            this.position += 1;
        }
    }
}

class ElevatorView {
    constructor(floors, people){
        this.elevator = document.querySelector('.elevator');
        for (let i=0; i < floors; i++) {
            let floor = document.createElement('li');
            floor.classList.add('floor');
            this.elevator.appendChild(floor);
        }
        this.floors = document.querySelectorAll('li');
        this.floors[floors-1].classList.add('selected');
        this.floors[floors-1].textContent = 0;
    }

    update(people, position) {
        this.floors.forEach(function(e){
            if (e.classList.contains('selected')) {
                e.classList.remove('selected');
                e.textContent = '';
            }
        });
        this.floors[position-1].textContent = people;
        this.floors[position-1].classList.add('selected');
    }
}

class ElevatorController {
    constructor(maxfloor, maxpeople){
        this.model = new ElevatorModel(maxfloor, maxpeople);
        this.view = new ElevatorView(maxfloor, maxpeople, this);
        this.add = document.querySelector('.add');
        this.add.addEventListener('click', function (){
            this.eventHandler(this.model.addPeople);
        }.bind(this));
        this.remove = document.querySelector('.remove');
        this.remove.addEventListener('click', function (){
            this.eventHandler(this.model.removePeople);
        }.bind(this));
        this.up = document.querySelector('.up');
        this.up.addEventListener('click', function (){
            this.eventHandler(this.model.elevatorUp);
        }.bind(this));
        this.down = document.querySelector('.down');
        this.down.addEventListener('click', function (){
            this.eventHandler(this.model.elevatorDown);
        }.bind(this));
    }
    
    eventHandler(action) {
        action.bind(this.model)();
        this.view.update(this.model.people, this.model.position);
    }
}

let lift = new ElevatorController(10, 10);