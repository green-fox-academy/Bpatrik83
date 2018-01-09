'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer() {
    let result = [];
    for (let i = 0; i < arguments.length; i++) {
        result.push(arguments[i]);
    }
    return result;
}

console.log(printer(1, 2, 3, 4 ,5 , 6, 7, 8, 9, 10));