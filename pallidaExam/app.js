'use strict'

const mysql = require("mysql");
const conn = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "root",
  database: "licence_plates"
});

function createMySqlConnection() {
  conn.connect(function (err) {
    if (err) {
      console.log("Error connecting to Db");
      return;
    }
    console.log("Connection established");
  });
}

function middleWare() {
}
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Username");
  next();
});

function searchEndPoint() {
  app.get('/search', function (req, res) {
      if (dataValidator(req.query)) {
        conn.query(`SELECT * FROM licence_plates WHERE plate LIKE '${req.query.q}%';`, function (err, rows) {
          if (rows.length === 0) {
            res.json({"result": "notFound", "message": "invalid input"});
          } else {
            res.json(formatDataToSend(rows));
          }
        });
      } else {
        res.json({"result": "error", "message": "invalid input"});
      }
    }
  );
}

function brandEndPoint() {
  app.get('/search/:brand', function (req, res) {
    conn.query(`SELECT * FROM licence_plates WHERE car_brand LIKE '${req.params.brand}';`, function (err, rows) {
        res.json(formatDataToSend(rows));
      }
    );
  });
}

function formatDataToSend(data) {
  return {result: 'OK', data: data};
}

function dataValidator(data) {
  return (data.q.length < 8 && data.q.match(/^[a-z0-9-]+$/i) && data.q.length !== 0);
}

createMySqlConnection();
searchEndPoint();
brandEndPoint();

app.listen(8080, function () {
  console.log('the app is running');
});