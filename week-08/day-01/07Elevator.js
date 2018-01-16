class ElevatorController {

    constructor(height) {
        this.elevatorPosition = 1;
        this.houseHeight = height;
        this.buttonUp = document.querySelector('.up');
        this.buttonDown = document.querySelector('.down');
    }

    moveUp() {
        view.clearFloor(`.floor${this.elevatorPosition}`);
        this.elevatorPosition < this.houseHeight ? this.elevatorPosition++ : this.elevatorPosition;
        view.drawCurrentFloor(`.floor${this.elevatorPosition}`);
    }

    moveDown() {
        view.clearFloor(`.floor${this.elevatorPosition}`);
        this.elevatorPosition > 1 ? this.elevatorPosition-- : this.elevatorPosition;
        view.drawCurrentFloor(`.floor${this.elevatorPosition}`);
    }

    moveElevator() {
        this.buttonUp.onclick = this.moveUp.bind(this);
        this.buttonDown.onclick = this.moveDown.bind(this);
    }



}

class ElevatorModel {

    constructor() {
        this.peopleNumber = 0;
        this.addPeopleButton = document.querySelector('.addPeople');
        this.removePeopleButton = document.querySelector('.removePeople');
    }

    addPeople() {
        this.peopleNumber < 10 ? this.peopleNumber++ : this.peopleNumber;
        view.currenPeople(this.peopleNumber);
    }

    removePeople() {
        this.peopleNumber > 0 ? this.peopleNumber-- : this.peopleNumber;
        view.currenPeople(this.peopleNumber);
    }

    addPeopleToElevator() {
        this.addPeopleButton.onclick = this.addPeople.bind(this);
        this.removePeopleButton.onclick = this.removePeople.bind(this);
    }
}

class ElevatorView {

    constructor(maxHeight) {
        this.floorHeight = maxHeight;
    }

    drawFloors() {
        for (let i = this.floorHeight; i > 0  ; i--) {
            document.querySelector('.elevator').innerHTML += `<div class="floor${i} floor"></div>`
        }
    }

    clearFloor(floor) {
        document.querySelector(floor).innerHTML = '';
        document.querySelector(floor).style.backgroundColor = 'white';
    }

    drawCurrentFloor(floor) {
        document.querySelector(floor).innerHTML = model.peopleNumber;
        document.querySelector(floor).style.backgroundColor = 'green';


    }

    currenPeople(people) {
        document.querySelector(`.floor${controller.elevatorPosition}`).innerHTML = model.peopleNumber;
    }
}

let height = 10;
let view = new ElevatorView(height);
let controller = new ElevatorController(height);
model = new ElevatorModel();
model.addPeopleToElevator();
view.drawFloors();
view.drawCurrentFloor('.floor1');
controller.moveElevator();




