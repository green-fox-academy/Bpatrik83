'use strict';

let test = require('tape');
let letterFrequency = require('./countletters');

test('empty text', function (t) {
  let actual = letterFrequency('');
  let expected = {};

  t.deepEqual(actual, expected);
  t.end();
});

test('one letter', function (t) {
  let actual = letterFrequency('a');
  let expected = {a: 1};

  t.deepEqual(actual, expected);
  t.end();
});

test('numbers', function (t) {
  let actual = letterFrequency('112343452');
  let expected = {};

  t.deepEqual(actual, expected);
  t.end();
});

test('special characters', function (t) {
  let actual = letterFrequency(`"+!%/=()>;2'`);
  let expected = {};

  t.deepEqual(actual, expected);
  t.end();
});

test('different letters', function (t) {
  let actual = letterFrequency('abcabcabc');
  let expected = {a: 3, b: 3, c: 3};

  t.deepEqual(actual, expected);
  t.end();
});