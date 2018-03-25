'use strict';

function connnect(method, query, endPoint, callback) {
  const xhr = new XMLHttpRequest(),
    method = method,
    url = `http://localhost:8080/${endPoint}${query}`;
  xhr.open(method, url);
  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
}

function showDatasInDOM(datas) {
  document.querySelector('table').innerHTML =
    `<tr>
    <th>Item Name</th>
    <th>Manufacturer</th>
    <th>Category</th>
    <th>Size</th>
    <th>Unit price</th>
  </tr>`;
  datas.clothes.forEach(function (item) {
    document.querySelector('table').innerHTML +=
      `<tr>
        <td>${item.item_name}</td>
        <td>[${item.manufacturer}]</td>
        <td>${item.category}</td>
        <td>${item.size}</td>
        <td>${item.unit_price}</td>
      </tr>`;
  });
}

function addEventToButtons() {
  document.querySelector('button').addEventListener('click', getTotal);
}

function getTotal(event) {

}

connnect('GET', '', 'warehouse', showDatasInDOM);
