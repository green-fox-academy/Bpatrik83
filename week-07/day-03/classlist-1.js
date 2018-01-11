'use strict';

let thirdPClass = document.querySelectorAll('p')[2].className;
if (thirdPClass.includes('red-dot')) {
    alert('OMG DOTS!');
}

let fourthPClass = document.querySelectorAll('p')[3].className;
if (fourthPClass.includes('dolphin')) {
    document.getElementsByClassName('apple')[0].className = 'pear';
}

let firstPClass = document.querySelectorAll('p')[0].className;
if (firstPClass.includes('apple')) {
    document.getElementsByClassName('cat')[0].textContent = 'dog';
}

document.getElementsByClassName('apple')[0].className += ' red';

document.getElementsByClassName('balloon')[0].style.borderRadius = '1%';

console.log(document.getElementsByClassName('apple')[0]);
