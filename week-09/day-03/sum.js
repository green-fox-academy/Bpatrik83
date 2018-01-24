'use strict'

function sum(list) {
  let sum = 0;
  list.forEach(number => {
    if (typeof number !== 'number') {
      throw new Error(`'${number}' is not a number`);
    }
    sum += number;
  });
  return sum;
}

console.log(sum([1, 2, 3, 4, 5]));

module.exports = sum;
