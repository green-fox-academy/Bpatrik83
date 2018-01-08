'use strict';

let lineCount = 4;
let star = '*';

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for (let i = 0; i < lineCount; i++) {
    console.log(star);
    star += '*';
}
