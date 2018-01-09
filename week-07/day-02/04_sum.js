'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(num) {
     return num === 0 ? num : (num + sum(num - 1));
}

console.log(sum(10));