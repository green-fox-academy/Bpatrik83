

const audiosId = [];
let audioPosition = 0;

function connnect(query, callback) {
  const xhr = new XMLHttpRequest(),
    method = 'GET',
    url = `http://localhost:8080/${query}`;
  xhr.open(method, url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
}

function getMinutesToSeconds(seconds) {
  if (Math.floor(seconds - (Math.floor(seconds / 60) * 60)) < 10) {
    return `${Math.floor(seconds / 60)}:0${Math.floor(seconds - (Math.floor(seconds / 60) * 60))}`;
  }
  return `${Math.floor(seconds / 60)}:${Math.floor(seconds - (Math.floor(seconds / 60) * 60))}`;
}

function showAllDataByAudio(data) {
  const audioInfo = document.querySelector('.audioInformation');
  audioInfo.innerHTML = `<p>Album: ${data[0].album}</p><p>Album Artist: ${data[0].albumartist}</p>
  <p>Year: ${data[0].year}</p><p>Title: ${data[0].title}</p><p>Genre: ${data[0].genre}</p>`;
  document.querySelector('audio').setAttribute('src', data[0].url);
  audioPosition = data[0].id;
}

function changeBackgroundColor(element) {
  if (!document.querySelector('.pushed')) {
    element.className += ' pushed';
  } else {
    document.querySelector('.pushed').className = 'dataBox';
    element.className += ' pushed';
  }
}

function checkedCurrentAudio(idNumber) {
  connnect(`search?q=${idNumber}`, showAllDataByAudio);
  changeBackgroundColor(document.getElementById(`${idNumber}`));
}

function previousAudio() {
  if (audiosId[0] < audioPosition) {
    audioPosition += 1;
  }
  checkedCurrentAudio(audioPosition);
}

function nextAudio() {
  if (audiosId[audiosId.length - 1] > audioPosition) {
    audioPosition += 1;
  }
  checkedCurrentAudio(audioPosition);
}

function shuffle() {
  const randomId = audiosId[Math.floor(Math.random() * audiosId.length)];
  checkedCurrentAudio(randomId);
}

function clickDataBox(event) {
  connnect(`search?q=${event.target.getAttribute('id')}`, showAllDataByAudio);
  changeBackgroundColor(event.target);
}

function addEventToDataBoxes() {
  const className = document.getElementsByClassName('dataBox');
  Array.from(className).forEach((element) => {
    element.addEventListener('click', clickDataBox);
  });
}

function addEventToButtons() {
  document.querySelector('.previous').addEventListener('click', previousAudio);
  document.querySelector('.next').addEventListener('click', nextAudio);
  document.querySelector('.shuffle').addEventListener('click', shuffle);
}

function showAlbumList(datas) {
  datas.forEach((item) => {
    document.querySelector('.right').innerHTML += `<div class="dataBox" id="${item.id}"><p>${item.title}</p> <p>${getMinutesToSeconds(item.duration)}</p></div>`;
    audiosId.push(item.id);
  });
  addEventToDataBoxes();
  addEventToButtons();
  changeBackgroundColor(document.getElementById(`${audiosId[0]}`));
  showAllDataByAudio(datas);
}

connnect('', showAlbumList);
