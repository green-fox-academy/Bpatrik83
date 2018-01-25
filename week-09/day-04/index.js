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
  if (req.query.input !== 'undefined') {
    res.json({
      "received": req.query.input,
      "result": req.query.input * 2
    });
  } else {
    res.json({
      "error": "Please provide an input!"
    });
  }
});

app.listen(8080, function () {
  console.log('the app is running');
});