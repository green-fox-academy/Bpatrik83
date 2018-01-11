'use strict';

alert(document.getElementsByTagName('h1'));
console.log(document.querySelector('p'));
alert(document.querySelector('.other'));
document.getElementsByTagName('h1')[0].innerHTML = "New content";
document.querySelector('.result').innerHTML = document.querySelector('p').innerHTML;