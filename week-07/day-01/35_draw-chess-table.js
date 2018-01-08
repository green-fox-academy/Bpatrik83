'use strict';

let chessTableSize = 5;

if (chessTableSize % 2 !== 0) {
    chessTableSize++;
}

// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
//


for (let i = 0; i < chessTableSize; i++) {
    if (i % 2 === 0) {
        console.log('% '.repeat(chessTableSize / 2));
    } else {
        console.log(' %'.repeat(chessTableSize / 2));
    }
}