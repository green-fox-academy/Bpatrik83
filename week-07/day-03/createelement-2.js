'use strict';

let candyShop = document.getElementsByClassName('candyshop')[0];
let megaJuicy = document.querySelector('li');

candyShop.removeChild(megaJuicy);

for (let i = 1; i <= 16; i++) {
    let tempChild = document.createElement('li');
    tempChild.textContent = 'Empty box #' + i;
    candyShop.appendChild(tempChild);
}
