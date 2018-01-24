'use strict';

let test = require('tape');
let myObject = require('./apples.js');

test('get apples', function (t) {
  let actual = myObject.getApple();
  let expected = 'apple';

  t.equal(actual, expected);
  t.end();
});