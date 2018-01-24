'use strict';

function letterFrequency(text) {
  let count = {};
  text.split('').filter(char => {
    return char.toLowerCase().match(/[a-z]/i);
  }).forEach(function (char) {
    count[char] = count[char] ? count[char] + 1 : 1;
  });
  return count;
}

console.log(letterFrequency('wklv lv d vhfuhw phvvdjh e r 1 34 45 ! + "'));

module.exports = letterFrequency;
