'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.post('/arrays', function (req, res) {
    res.json(checkInput(req.body.what, req.body.numbers));
  }
);

function sum(numbers) {
  let result = 0;
  numbers.forEach(number => result += number);
  return result;
}

function multiply(numbers) {
  let result = 1;
  numbers.forEach(number => result *= number);
  return result;
}

function doubling(numbers) {
  return numbers.map(number => number * 2);
}

function errorHandling(what, numbers) {
  return (what !== 'sum' && what !== 'multiply' && what !== 'double' || numbers.length === 0);
}

function checkInput(what, numbers) {
  if (errorHandling(what, numbers)) {
    return {
      "error": "Please provide what to do with the numbers!"
    };
  }
  else if (what === 'sum') {
    return {"result": sum(numbers)};
  }
  else if (what === 'multiply') {
    return {"result": multiply(numbers)};
  }
  else if (what === 'double') {
    return {"result": doubling(numbers)};
  }
}

app.listen(8080, function () {
  console.log('the app is running');
});
