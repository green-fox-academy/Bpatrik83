function connnect(query, endPoint, callback) {
  const xhr = new XMLHttpRequest(),
    method = 'GET',
    url = `http://localhost:8080/${endPoint}${query}`;
  xhr.open(method, url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
}

function showDatasOnPage(datas) {
  createUniqList(datas.clothes);
  document.querySelector('table').innerHTML =
    `<tr>
    <th>Item Name</th>
    <th>Manufacturer</th>
    <th>Category</th>
    <th>Size</th>
    <th>Unit price</th>
  </tr>`;
  datas.clothes.forEach((item) => {
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

function createUniqList(datas) {
  let uniqeNames = [];
  let uniqeSize = [];
  datas.forEach((item) => {
    if (!uniqeNames.includes(item.item_name)) {
      uniqeNames.push(item.item_name);
    }
    if (!uniqeSize.includes(item.size)) {
      uniqeSize.push(item.size);
    }
  });
  showNames(uniqeNames);
  showSize(uniqeSize);
}

function showNames(names) {
  names.forEach(function (name) {
    document.querySelector('.itemName').innerHTML += `
    <option value='${name}'>${name}</option>`
  });
}

function showSize(sizes) {
  sizes.forEach((size) => {
    document.querySelector('.itemSize').innerHTML += `
    <option value='${size}'>${size}</option>`
  });
}

function addEventToButtons() {
  document.querySelector('button').addEventListener('click', getTotal);
}

function getTotal(event) {
  let itemName = document.querySelector('.itemName').value;
  let itemSize = document.querySelector('.itemSize').value;
  let itemQuantity = document.querySelector('input').value;
  connnect('', `price-check/?item=${itemName}&size=${itemSize}&quantity=${itemQuantity}`, showBackEndMessage);
}

function showBackEndMessage(datas) {
  if (datas.result === 'ok') {
    document.querySelector('.message').innerHTML = `<p class="ok">The items can be ordered, the total price is: ${datas.total_price}</p>`;
  } else {
    document.querySelector('.message').innerHTML = `<p class="error">${datas.result}</p>`;
  }

}

connnect('', 'warehouse', showDatasOnPage);
addEventToButtons();