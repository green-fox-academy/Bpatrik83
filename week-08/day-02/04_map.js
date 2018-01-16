'use strict';

var fruits = [
    'melon',
    'apple',
    'strawberry',
    'blueberry',
    'pear',
    'banana'
];

let eCounter = fruits.map(fruit => fruit.match(/e/gi).map(item => console.log(item.length)));
console.log(eCounter);

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.
