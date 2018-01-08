'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let aSide = 10;
let bSide = 10;
let cSide = 10;

let surface = 2 * ((aSide * bSide) + (aSide * cSide) + (bSide * cSide));
let volume = (aSide * bSide * cSide);

console.log(`Surface Area: ${surface}`);
console.log(`Volume: ${volume}`);