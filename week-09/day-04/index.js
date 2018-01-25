'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.use('/assets', express.static('assets'));

app.get('/', function (req, res) {
  res.sendfile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  if (typeof req.query.input !== 'undefined') {
    res.json({
      "received": Number(req.query.input),
      "result": Number(req.query.input) * 2
    });
  } else {
    res.json({
      "error": "Please provide an input!"
    });
  }
});

app.get('/greeter', function (req, res) {
  if (typeof req.query.name !== 'undefined' && typeof req.query.title !== 'undefined') {
    res.json({
      "welcome_message": `Oh, hi there ${req.query.name}, my dear ${req.query.title}!`
    });
  } else if (typeof req.query.name === 'undefined' && typeof req.query.title === 'undefined') {
    res.json({
      "error": "Please provide a name!"
    });
  } else {
    res.json({
      "error": "Please provide a title!"
    });
  }
});

app.get('/appenda/:data', function (req, res) {
  res.json({
    "appended": `${req.params.data}a`
  });
});

app.post('/dountil/:data', function (req, res) {
  if (req.params.data === 'sum') {
    res.json({"result": numberSum(req.body.until)});
  } else if (req.params.data === 'factor') {
    res.json({"result": factorialize(req.body.until)});
  }
});

function numberSum(number) {
  if (number <= 0)
    return 0;
  else {
    return (number + numberSum(number - 1));
  }
}

function factorialize(number) {
  if (number < 0)
    return -1;
  else if (number == 0)
    return 1;
  else {
    return (number * factorialize(number - 1));
  }
}

app.listen(8080, function () {
  console.log('the app is running');
});