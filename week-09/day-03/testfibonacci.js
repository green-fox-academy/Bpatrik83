'use strict';

let test = require('tape');
let fibonacci = require('./fibonacci.js');

test('zero', function (t) {
  let actual = fibonacci(0);
  let expected = 0;

  t.deepEqual(actual, expected);
  t.end();
});

test('valid number', function (t) {
  let actual = fibonacci(25);
  let expected = 75025;

  t.deepEqual(actual, expected);
  t.end();
});

test('not a number', function (t) {
  t.throws(fibonacci.bind(this, 'a'), Error);
  t.end();
});
