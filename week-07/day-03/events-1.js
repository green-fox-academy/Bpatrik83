'use strict';

let button = document.getElementsByTagName('button')[0];
let bodyBack = document.getElementsByTagName('body')[0];

function backChange() {
    bodyBack.setAttribute('class', 'party');
}

button.onclick = backChange;

console.log(button)

console.log(document.getElementsByTagName('body'));