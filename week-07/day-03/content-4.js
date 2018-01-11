'use strict';

let randomWords = ['apple', 'banana', 'cat', 'dog'];
for (let i = 0; i < randomWords.length; i++) {
    document.querySelectorAll('li')[i].innerHTML = randomWords[i];
    document.querySelectorAll('li')[i].style.backgroundColor = 'limegreen';
}
