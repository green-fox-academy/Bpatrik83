'use strict';

let lineCount = 20;
let squareChar = '%';

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

console.log(squareChar.repeat(lineCount));
for (let i = 0; i < lineCount - 2; i++) {
    console.log(squareChar + ' '.repeat(i) + squareChar + ' '.repeat( lineCount - i - 3) + squareChar);
}
console.log(squareChar.repeat(lineCount));
