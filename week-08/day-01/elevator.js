class ElevatorModel {
    constructor(maxfloor, maxpeople){
        this.maxfloor = maxfloor;
        this.maxpeople = maxpeople;
        this.position = 10;
        this.direction = '';
        this.people = maxpeople;
    }

    checkLimits(action){
        if (action === 'add') {
            return this.people < this.maxpeople;
        } else if (action === 'remove') {
            return this.people > 0;
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
        this.floors[floors-1].textContent = people;
    }

    update(people, position) {
        this.floors[position-1].textContent = people;
    }
}

class ElevatorController {
    constructor(maxfloor, maxpeople){
        this.model = new ElevatorModel(maxfloor, maxpeople);
        this.view = new ElevatorView(maxfloor, maxpeople, this);
        this.add = document.querySelector('.add');
        this.add.addEventListener('click', this.addPeople.bind(this));
        this.remove = document.querySelector('.remove');
        this.remove.addEventListener('click', this.removePeople.bind(this));
    }
    
    addPeople() {
        this.model.addPeople();
        this.view.update(this.model.people, this.model.position);
    }

    removePeople() {
        this.model.removePeople();
        this.view.update(this.model.people, this.model.position);
    }
}

let lift = new ElevatorController(10, 10);