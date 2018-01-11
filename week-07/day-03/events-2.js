'use strict';

let button = document.getElementsByTagName('button')[0];
let result = document.getElementsByClassName('result')[0];

console.log();

function changeText() {
    result.textContent = document.querySelectorAll('li').length;
}

button.onclick = changeText;



