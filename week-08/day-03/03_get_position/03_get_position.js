let uluru = {lat: -25.363, lng: 131.044};

function findMap(cityLocation = {lat: -25.363, lng: 131.044}) {
    let uluru = cityLocation;
    let map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: uluru
    });
    let marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}

function requestMap(url) {
    let request = new XMLHttpRequest;
    request.open('GET', url, true);
    request.send();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            let data = JSON.parse(request.responseText);
            findMap(data.results[0].geometry.location);
        } else {
            console.log('reached google, but API returned an error');
        }
    };
    request.onerror = function() {
        console.log('connection error');
    };
}

function clickButton() {
    document.querySelector('button').onclick = getCityName;
}

function getCityName() {
    createUrl(document.querySelector('input').value);
}

function createUrl(cityName) {
    let url = `https://maps.googleapis.com/maps/api/geocode/json?address=${cityName}&key=AIzaSyC0BvLt2BKY6ZTyz-OqvSuqJgB8Gc5gfp0`;
    requestMap(url);
}
setTimeout(function () {
    findMap(uluru);
}, 10);

clickButton();
