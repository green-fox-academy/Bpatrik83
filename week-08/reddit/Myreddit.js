'use strict';

function requestReddit(url) {
  let request = new XMLHttpRequest();
  request.open('GET', url);
  request.onerror = () => {
    console.log('connection error');
  }
  request.send();
  request.onload = () => {
    request.status === 200 ? loadPost(JSON.parse(request.responseText).posts) : console.log('Status not 200!');
  };
}

function connection(method, url) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200 ? changeDatas(JSON.parse(xhr.responseText), method) : console.log('We have some problem :( !');
  }
  xhr.send();
}
function changeDatas(data, method) {
  method === 'PUT' ? document.querySelector(`var[data-id="${data.id}"]`).innerHTML = `${data.score}` :
    document.querySelector(`.section${data.id}`).remove();
}

function loadPost(data) {
  let article = document.querySelector('article');
  data.forEach(function (item) {
    article.insertBefore(createElement(item), article.firstChild);
    upVote(item.id);
    downVote(item.id);
    deleteButton(item.id);
  });
}

function createDomString(item) {
  let domString = `
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
  return domString;
}

function createElement(item) {
  let post = document.createElement('section');
  post.setAttribute('class', `post section${item.id}`);
  post.innerHTML = createDomString(item);
  return post;
}

function deleteButton(itemId) {
  document.querySelector('.delete').addEventListener('click', function () {
    connection('DELETE', `https://time-radish.glitch.me/posts/${itemId}`);
  });
}

function upVote(itemId) {
  document.querySelector('.buttonUp').addEventListener('click', function () {
    connection('PUT', `https://time-radish.glitch.me/posts/${itemId}/upvote`);
  });
}

function downVote(itemId) {
  document.querySelector('.buttonDown').addEventListener('click', function () {
    connection('PUT', `https://time-radish.glitch.me/posts/${itemId}/downvote`);
  });
}

function convertTime(timestamp) {
  let pubDate = new Date();
  pubDate.setTime(timestamp);
  let weekday = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
  let monthname = new Array("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec");
  return `${weekday[pubDate.getDay()]}, ${monthname[pubDate.getMonth()]}, ${pubDate.getDate()}, ${pubDate.getUTCFullYear()}`;
}

requestReddit('https://time-radish.glitch.me/posts');
