'use strick';

document.addEventListener('DOMContentLoaded', submitClick, false);

function submitClick() {
  let submitButton = document.querySelector('.submitButton');
  submitButton.addEventListener('click', getDatas, true);
};

function getDatas() {
  let title = document.querySelector('.title');
  let url = document.querySelector('.url');
  title.value === '' ? alert('Please fill the title field!') : textFormatting(title.value, url.value);
}

function textFormatting(title, url) {
  postMessage({"title": title, "url": url});
}

function postMessage(message) {
  let url = 'http://localhost:8080/posts';
  let xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200 ? console.log('ready!') : console.log('We have some problem :( !');
  }
  xhr.send(JSON.stringify(message));
  window.location = 'index.html';
}


