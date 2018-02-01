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

app.get('/price-check/', (req, res) => {
  conn.query(`SELECT unit_price, in_store FROM warehouse WHERE item_name = '${req.query.item}' AND size = '${req.query.size}';`, (err, rows) => {
    res.send(checkQueryData(rows, req.query.quantity));
    console.log(err);
  });
});

function checkQueryData(item, quantity) {
  if (quantity < 3) {
    return {
      'result': 'please order at least 3, one for yourself, two for your friends'
    }
  } else if (quantity > item[0].in_store) {
    return {
      "result": "error, we don't have enough items in store"
    }
  } else {
    return {
      "result": "ok",
      "total_price": quantity * item[0].unit_price
    }
  }
}

app.listen(8080, () => {
  console.log('The app is running');
});