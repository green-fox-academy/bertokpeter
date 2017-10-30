class ElevatorModel {
    constructor(maxfloor, maxpeople){
        this.maxfloor = maxfloor;
        this.maxpeople = maxpeople;
    }
}

class ElevatorView {
    constructor(floors){
        this.elevator = document.querySelector('.elevator');
        for (let i=0; i < floors; i++) {
            let floor = document.createElement('li');
            floor.classList.add('floor');
            this.elevator.appendChild(floor);
        }
    }
}

class ElevatorController {
    constructor(maxfloor, maxpeople){
        this.model = new ElevatorModel(maxfloor, maxpeople);
        this.view = new ElevatorView(this.model.maxfloor);
    }
}

let lift = new ElevatorController(10, 10);