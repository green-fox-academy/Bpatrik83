'use strict';

let test = require('tape');
let sum = require('./sum.js');

test('two numbers sum', function (t) {
  let actual = sum([1, 2]);
  let expected = 3;

  t.equal(actual, expected);
  t.end();
});

test('empty list', function (t) {
  let actual = sum([]);
  let expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('more numbers sum', function (t) {
  let actual = sum([1, 2, 3, 4, 5]);
  let expected = 15;

  t.equal(actual, expected);
  t.end();
});

test('not a number', function (t) {

  t.throws(sum.bind(this, ['a']), Error);
  t.end();
});