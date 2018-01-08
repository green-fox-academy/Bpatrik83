'use strict';

let lineCount = 4;
let star = '*';
let space = ' ';

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (let i = lineCount; i > 0; i--) {
    console.log(space.repeat(i) + star);
    star += '**';
}
