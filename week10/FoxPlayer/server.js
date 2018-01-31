

const mysql = require('mysql');

const conn = mysql.createConnection({
  host: 'localhost',
  user: "'root'",
  password: 'root',
  database: 'audiodatas',
});

conn.connect((err) => {
  if (err) {
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

function showAll() {
  conn.query('SELECT * FROM music;', (err, rows) => {
    console.log(rows);
  });
}

function deleteAllrecords() {
  conn.query('DELETE FROM music;', (err, rows) => {
    console.log(err);
  });
}

function createTable(metaData, fileName, duration) {
  // console.log(metaData.picture[0]);
  // base64(metaData.picture[0].data);
  // const albumPic = new Buffer(metaData.picture[0].data).toString('base64');
  // console.log('image: ', albumPic.length);
  conn.query(`INSERT INTO music (albumartist, title, artist, album, year, genre, url, duration) VALUES ('${metaData.albumartist}', '${metaData.title.replace('\'', '\'\'')}'
  , '${metaData.artist.replace('\'', '\'\'')}', '${metaData.album.replace('\'', '\'\'')}', '${metaData.year}', '${metaData.genre}', 
  'assets/${fileName}', '${duration}')`, (err, rows) => {
  });
}

function getMetaData(fileName) {
  const mm = require('music-metadata');
  const util = require('util');
  mm.parseFile(`assets/${fileName}`, { native: true })
    .then((metadata) => {
      createTable(metadata.common, fileName, metadata.format.duration);
    })
    .catch((err) => {
      console.error(err.message);
    });
}

function getFileNames() {
  const fs = require('fs');
  const files = fs.readdirSync('assets/');
  files.forEach((fileName) => {
    getMetaData(fileName);
  });
}


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

function firstEndPoint() {
  app.get('/', (req, res) => {
    conn.query('SELECT * FROM music;', (err, rows) => {
      res.send(rows);
    });
  });
}

function getDataByID() {
  app.get('/search', (req, res) => {
    conn.query(`SELECT * FROM music WHERE id = '${req.query.q}';`, (err, rows) => {
      res.send(rows);
    });
  });
}

// deleteAllrecords();
// getFileNames();
// showAll();
firstEndPoint();
getDataByID();


app.listen(8080, () => {
  console.log('the app is running');
});
