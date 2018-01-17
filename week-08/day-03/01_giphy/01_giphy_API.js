'use strict'

document.addEventListener('DOMContentLoaded', function () {



    function requestGif() {
        let q = "q=finger+guns";
        let request = new XMLHttpRequest;
        request.open('GET', `http://api.giphy.com/v1/gifs/search?${q}&api_key=TXzHJEXDfA1qFJeeMDe9YbabKgkHbFEb&limit=16`, true);
        request.send();
        request.onload = function () {
            if (request.status >= 200 && request.status < 400) {
                let data = JSON.parse(request.responseText).data;
                drawGifs(data);
                clickGifs(document.querySelectorAll('div'));
            } else {
                console.log('reached giphy, but API returned an error');
            }
        };
        request.onerror = function() {
            console.log('connection error');
        };
    }

    function drawGifs(listOfGifs) {
        listOfGifs.map(gif => document.querySelector('main').innerHTML += `<div><img src='${gif.images.fixed_width_small_still.url}'></div>`);
    }

    function clickGifs(listOfGifs) {
        listOfGifs.forEach(function (gif) {
            gif.onclick = onPictureClick;
        });
    }

    function onPictureClick(event) {
        event.target.src = event.target.src.replace('_s', '');
    }

    requestGif();
});