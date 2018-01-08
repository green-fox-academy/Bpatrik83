
'use strict';

let lineCount = 6;
let squareChar = '%';

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

console.log(squareChar.repeat(lineCount));
for (let i = 0; i < lineCount - 2; i++) {
    console.log(squareChar + ' '.repeat(lineCount - 2) + squareChar);
}
console.log(squareChar.repeat(lineCount));