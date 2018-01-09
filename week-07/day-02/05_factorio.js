'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorial(num) {
    return num == 0 ? 1 : num * factorial(num - 1)
}

console.log(factorial(8));
