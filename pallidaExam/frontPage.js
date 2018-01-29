'use strict';

function connnect(query) {
  let xhr = new XMLHttpRequest(),
    method = 'GET',
    url = `http://localhost:8080/search${query}`;
  xhr.open(method, url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      showDataInDom(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
}

function createQuery(query) {
  if (document.querySelector('.police').checked) {
    query = `?q=rb`;
  } else if (document.querySelector('.diplomat').checked) {
    query = `?q=dt`;
  } else {
    query = `?q=${query}`;
  }
  connnect(query);
}

function getInputData() {
  createQuery(document.querySelector('.field').value);
}

function showDataInDom(datas) {
  if (datas.result === 'notFound') {
    document.querySelector('table').innerHTML = 'Sorry, the submitted licence plate is not valid!';
  } else if (datas.result === 'error') {
    document.querySelector('table').innerHTML = 'Sorry, wrong text format!';
  } else {
    createTable(datas.data);
  }
}

function queryButtonClick() {
  document.querySelector('.queryButton').addEventListener('click', getInputData);
}

function createTable(data) {
  document.querySelector('table').innerHTML =
    `<tr>
    <th>Licence Plate</th>
    <th>Brand</th>
    <th>Model</th>
    <th>Color</th>
    <th>Year</th>
  </tr>`;
  data.forEach(function (car) {
    document.querySelector('table').innerHTML +=
      `<tr>
        <td>${car.plate}</td>
        <td class="brand" src="${car.car_brand}">[${car.car_brand}]</td>
        <td>${car.car_model}</td>
        <td>${car.color}</td>
        <td>${car.year}</td>
      </tr>`;
  });
  addEventToBrands();
}

function addEventToBrands() {
  let className = document.getElementsByClassName('brand');
  Array.from(className).forEach(function (element) {
    element.addEventListener('click', clickBrand);
  });
}

function clickBrand(event) {
  connnect(`/${event.target.getAttribute('src')}`);
}

queryButtonClick();
