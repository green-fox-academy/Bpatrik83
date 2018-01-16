'use stric'

/*Create an Animal constructor function

Every animal has a hunger property, which is a number
Every animal has a thirst property, which is a number
When creating a new animal object these properties are created with the default 5 value
Every animal can eat() which decreases their hunger by one
Every animal can drink() which decreases their thirst by one
Every animal can play() which increases both by one

Create a Farm constructor function

The farm has slots which defines the number of free places for animals
    The farm has list of Animals
The farm can breed() which creates a new animal if there's place for it
The farm can slaughter() which removes the least hungry animal
The farm can print reports about their current state:
    The farm has 11 living animals we are bankrupt
The farm can progress from day to a new day by calling it's progress() method:
All animals should have their methods called randomly with 50% chance
    The farm should call its breed and slaughter method at the end of each day
The farm should print report at the end of each day
Print the number of sheeps
Print "bankrupt" if no animals left
Print "okay" if the number of animals is above zero and under the slot number
Print "full" if the number of animals are at the maximum allowed */

function Animal(){
    this.hunger = 5;
    this.thirst = 5;
    this.eat = function() {
        this.hunger -= 1;
    }
    this.drink = function() {
        this.thirst -= 1;
    }
    this.play = function() {
        this.hunger += 1;
        this.thirst += 1;
    }
}

function Farm(slots) {
    this.animals = [];
    for (let i = 0; i < slots; i++) {
        this.animals.push(sheep = new Animal());
    }
    this.breed = function () {
        if (this.animals.length < slots) {
            let sheep = new Animal();
            this.animals.push(sheep);
        } else {
            console.log('Full House!');
        }
    }
    this.slaughter = function () {
        let leastHungry = 0;
        let slaughAnimal = 0;
        this.animals.forEach(function (animal, index) {
            if (animal.hunger > leastHungry) {
                leastHungry = animal.hunger;
                slaughAnimal = index;
            }
        });
        this.animals.splice(slaughAnimal, 1);
    }
    this.progress = function () {
        console.log(`The farm has ${this.animals.length} living animals we are bankrupt`);
    }
}

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

function randomAnimalHealth() {
    SheepFarm.animals.forEach(function (animal) {
        let randomNumber = getRandomInt(3);
        randomNumber === 0 ? animal.eat()
            : randomNumber === 1 ? animal.play()
            : randomNumber === 2 ? animal.drink() : 0
    });
}

const button = document.querySelector('.checkFarm');
const progressButton = document.querySelector('.progress');
const slaughterButton = document.querySelector('.slaughter');
const breedButton = document.querySelector('.breed');

function printAnimals() {
    document.querySelector('main').innerHTML = '';
    SheepFarm.animals.forEach(function (animal, index) {
        document.querySelector('main').innerHTML += `<p style="font-size: small">${index + 1}. Sheep hunger: ${animal.hunger} thirst ${animal.thirst}</p>`
    });
}

button.onclick = function() {SheepFarm.progress(), randomAnimalHealth(), console.log(SheepFarm.animals)};
progressButton.onclick = function () {printAnimals()} ;
slaughterButton.onclick = function () {SheepFarm.slaughter()};
breedButton.onclick = function () {SheepFarm.breed()};

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full
