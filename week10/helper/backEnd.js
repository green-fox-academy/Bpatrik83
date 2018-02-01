'use strict';

const mysql = require('mysql');

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'clothing',
});

conn.connect((err) => {
  if (err) {
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Username');
  next();
});

app.get('/warehouse', (req, res) => {
  conn.query('SELECT * FROM warehouse;', (err, rows) => {
    res.send({
      'result': 'ok',
      'clothes': rows
    });
    console.log(err);
  });
});

app.post('/posts', (req, res) => {
  conn.query(`INSERT INTO posts (title, url) VALUES ('${req.body.title}', '${req.body.url}')`, (err, rows) => {
    res.send({
      'result': 'ok',
      'clothes': rows
    });
    console.log(err);
  });
});

app.listen(8080, () => {
  console.log('The app is running');
});
