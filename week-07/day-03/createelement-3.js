'use strict';

let ulAsteroids = document.getElementsByClassName('asteroids')[0];
let theKing = document.querySelector('li');

ulAsteroids.removeChild(theKing);

const planetData = [
    {
        category: 'inhabited',
        content: 'Foxes',
        asteroid: true
    },
    {
        category: 'inhabited',
        content: 'Whales and Rabbits',
        asteroid: true
    },
    {
        category: 'uninhabited',
        content: 'Baobabs and Roses',
        asteroid: true
    },
    {
        category: 'inhabited',
        content: 'Giant monsters',
        asteroid: false
    },
    {
        category: 'inhabited',
        content: 'Sheep',
        asteroid: true
    }
]

for (let i = 1; i <= planetData.length; i++) {
    if (planetData[i].asteroid) {
        let tempChild = document.createElement('li');
        tempChild.textContent = planetData[i].content;
        tempChild.className = planetData[i].category;
        ulAsteroids.appendChild(tempChild);
    }
}

console.log(document.getElementsByClassName('inhabited')[i]);