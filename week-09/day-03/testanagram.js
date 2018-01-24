'use strict';

let test = require('tape');
let anagram = require('./anagram.js');

test('not equal theirs length', function (t) {
  let actual = anagram('Dog', 'godd');
  let expected = false;

  t.equal(actual, expected);
  t.end();
});

test('equal theirs length but not anagram', function (t) {
  let actual = anagram('Dog', 'gof');
  let expected = false;

  t.equal(actual, expected);
  t.end();
});

test('anagram', function (t) {
  let actual = anagram('Protectional', 'Lactoprotein');
  let expected = true;

  t.equal(actual, expected);
  t.end();
});

test('not a string', function (t) {

  t.throws(anagram.bind(this, 11, 12), Error);
  t.end();
});