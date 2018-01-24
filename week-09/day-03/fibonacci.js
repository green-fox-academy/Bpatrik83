'use strict';

function fibonacci(number) {
  if (typeof number !== 'number') {
    throw new Error(`Not a number!`);
  }
  if (number < 1)
    return 0;

  if (number <= 2)
    return 1;

  return fibonacci(number - 1) + fibonacci(number - 2);
}

console.log(fibonacci(25));

module.exports = fibonacci;
