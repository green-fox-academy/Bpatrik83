'use strict';

function requestReddit(url, callback) {
  let request = new XMLHttpRequest();
  request.open('GET', url);
  request.onerror = () => {
    console.log('connection error');
  }
  request.send();
  request.onload = () => {
    request.status === 200 ? callback(JSON.parse(request.responseText), createElement) : console.log('Status not 200!');
  };
}

function connection(method, url) {

  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.onreadystatechange = function () {
    xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200 ? changeDatas(xhr.responseText, method) : console.log('We have some problem :( !');
  }
  xhr.send();
}
function changeDatas(data, method) {
  console.log(document.querySelector(`var[data-id="${data}"]`));
  method === 'PUT' ? document.querySelector(`var[data-id="${data}"]`).innerHTML = `${data.score}` :
    document.querySelector(`.section${data}`).remove();
}

function loadPost(data, callback) {
  console.log(data);
  let article = document.querySelector('article');
  data.forEach(function (item) {
    article.insertBefore(callback(item, createDomString), article.firstChild);
    upVote(item.id);
    downVote(item.id);
    deleteButton(item.id);
  });
}

function createDomString(item) {

  return domString;let domString = `
    <div class="buttons">
      <button class="buttonUp ${item.id}"></button>
      <var data-id="${item.id}" class="counter">${item.score}</var>
      <button class="buttonDown ${item.id}"></button>
    </div>
    <div class="text">
      <h1>${item.title}</h1>
      <a href="${item.url}">${item.url}</a>
      <p><span>${item.owner}</span><span class="date"> ${convertTime(item.timestamp)}</span><span class="delete"> delete</span></p>
    </div>`;
}

function createElement(item, callback) {
  let post = document.createElement('section');
  post.setAttribute('class', `post section${item.id}`);
  post.innerHTML = callback(item);
  return post;
}

function deleteButton(itemId) {
  document.querySelector('.delete').addEventListener('click', function () {
    connection('DELETE', `${url}/delete/${itemId}`);
  });
}

function upVote(itemId) {
  document.querySelector('.buttonUp').addEventListener('click', function () {
    connection('PUT', `${url}/upvote/${itemId}`);
  });
}

function downVote(itemId) {
  document.querySelector('.buttonDown').addEventListener('click', function () {
    connection('PUT', `${url}/downvote/${itemId}`);
  });
}

function convertTime(timestamp) {
  let pubDate = new Date();
  pubDate.setTime(timestamp);
  let weekday = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
  let monthname = new Array("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec");
  return `${weekday[pubDate.getDay()]}, ${monthname[pubDate.getMonth()]}, ${pubDate.getDate()}, ${pubDate.getUTCFullYear()}`;
}

const url = 'http://localhost:8080';

requestReddit(url, loadPost);
