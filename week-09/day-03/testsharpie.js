'use strict';

const test = require('tape');
const useSharpie = require('./sharpie.js');

test('add string instead of integer', function (t) {
  t.throws(useSharpie.bind(this, ('red', 11), 100, 31), Error);
  t.end();
});


