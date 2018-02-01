'use strict';

let mysql = require("mysql");
let sqlData;

let conn = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "root",
  database: "redditdatabase"
});

conn.connect(function (err) {
  if (err) {
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

conn.query("SELECT * FROM posts;", function (err, rows) {
  sqlData = rows;
});

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

app.get('/', function (req, res) {
    conn.query("SELECT * FROM posts;", function (err, rows) {
      sqlData = rows;
    });
    res.json(sqlData);
  }
);

app.post('/posts', function (req, res) {
    conn.query(`INSERT INTO posts (title, url) VALUES ('${req.body.title}', '${req.body.url}')`, function (err, rows) {
    });
    res.json(sqlData);
  }
);


app.delete('/delete/:data', function (req, res) {
    conn.query(`DELETE FROM posts WHERE id = ?`, [req.params.data], function (err, rows) {
    });
    res.send(req.params.data);
  }
);

app.put('/upvote/:data', function (req, res) {
    conn.query(`UPDATE posts SET score = score + 1 WHERE id = ?`, [req.params.data], function (err, rows) {
    });
    res.send(req.params.data);
  }
);

app.put('/downvote/:data', function (req, res) {
    conn.query(`UPDATE posts SET score = score - 1 WHERE id = ?`, [req.params.data], function (err, rows) {
      console.log(fields);
      res.send(rows);
    });
  }
);

app.listen(8080, function () {
  console.log('the app is running');
});