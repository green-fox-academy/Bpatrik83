function Animal() {
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function () {
    this.hunger -= 1;
  }
  this.drink = function () {
    this.thirst -= 1;
  }
  this.play = function () {
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

/*const button = document.querySelector('.checkFarm');
const progressButton = document.querySelector('.progress');
const slaughterButton = document.querySelector('.slaughter');
const breedButton = document.querySelector('.breed');

function printAnimals() {
  document.querySelector('main').innerHTML = '';
  SheepFarm.animals.forEach(function (animal, index) {
    document.querySelector('main').innerHTML += `<p style="font-size: small">${index + 1}. Sheep hunger: ${animal.hunger} thirst ${animal.thirst}</p>`
  });
}

button.onclick = function () {
  SheepFarm.progress(), randomAnimalHealth(), console.log(SheepFarm.animals)
};
progressButton.onclick = function () {
  printAnimals()
};
slaughterButton.onclick = function () {
  SheepFarm.slaughter()
};
breedButton.onclick = function () {
  SheepFarm.breed()
};
*/
// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full