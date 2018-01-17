function requestGif() {
    let url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=2b2f28dacf504f08bd4e62232876191c&q=moon+landing+Apollo+11';

    let request = new XMLHttpRequest;
    request.open('GET', url, true);
    request.send();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            let data = JSON.parse(request.responseText);
            writeDatas(data.response.docs[9]);
        } else {
            console.log('reached giphy, but API returned an error');
        }
    };
    request.onerror = function() {
        console.log('connection error');
    };
}

function writeDatas(datas) {
    console.log(datas);
    document.querySelector('ul').innerHTML += `<li>${datas.headline.main}</li>`;
    document.querySelector('ul').innerHTML += `<li>${datas.snippet}</li>`;
    document.querySelector('ul').innerHTML += `<li>${datas.pub_date}</li>`;
    document.querySelector('ul').innerHTML += `<li><a href='${datas.web_url}'>${datas.web_url}</a></li>`;

}

requestGif();