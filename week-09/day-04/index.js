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
  console.log(req.query.input);
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
  } else if(typeof req.query.name === 'undefined' && typeof req.query.title === 'undefined') {
    res.json({
      "error": "Please provide a name!"
    });
  } else {
    res.json({
      "error": "Please provide a title!"
    });
  }
});

app.listen(8080, function () {
  console.log('the app is running');
});