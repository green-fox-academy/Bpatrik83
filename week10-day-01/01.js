'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals() {
  this.AnimalSay = function (animalSay) {
    console.log(animalSay)
  };
}

let kutya = new Animals();

kutya.AnimalSay('Vau Vau');