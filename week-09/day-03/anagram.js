'use strict'

function anagram(stringOne, stringTwo) {
  if (typeof stringOne !== 'string' || typeof stringTwo !== 'string') {
    throw new Error('not a string');
  }
  if (stringOne.length !== stringTwo.length) {
    return false;
  }
  stringOne = stringOne.toLowerCase().split('').sort().join('');
  stringTwo = stringTwo.toLowerCase().split('').sort().join('');

  return stringOne === stringTwo ? true : false;
}

console.log(anagram('hello bello', 'bello olle'));

module.exports = anagram;
