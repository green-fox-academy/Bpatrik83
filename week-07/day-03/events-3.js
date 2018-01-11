'use strict';

let h1Text = document.querySelector('h1');

document.onkeypress = myFunction;

function myFunction(event) {
    let x = event.keyCode;
    h1Text.innerHTML = "Last pressed key code is: " + x;
}

document.addEventListener(myFunction());
