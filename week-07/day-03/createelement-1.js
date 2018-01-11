'use strict';

let greenFoxLi = document.createElement('li');
greenFoxLi.textContent = 'The Green Fox';
document.getElementsByTagName('ul')[0].appendChild(greenFoxLi);

let lampLighterLi = document.createElement('li');
lampLighterLi.textContent = 'The Lamplighter';
document.getElementsByTagName('ul')[0].appendChild(lampLighterLi);

let heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM!';
document.getElementsByClassName('container')[0].appendChild(heading);

let anyImage = document.createElement('img');
anyImage.setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/originals/77/5e/77/775e774ba9219063f4d48b5469c4fc65.jpg');
document.getElementsByClassName('container')[0].appendChild(anyImage);


console.log(document.getElementsByTagName('ul')[0]);