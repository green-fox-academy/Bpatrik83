'use strict';

console.log(document.getElementsByTagName('img')[0].getAttribute('src'));
document.getElementsByTagName('img')[0].setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/originals/77/5e/77/775e774ba9219063f4d48b5469c4fc65.jpg');
document.getElementsByTagName('a')[0].setAttribute('href', 'https://www.greenfoxacademy.com/');
document.getElementsByClassName('this-one')[0].disabled = true;
document.getElementsByClassName('this-one')[0].innerText = `Don't click me!`;
