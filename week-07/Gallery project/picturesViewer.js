'use strict';

const pics = [
    { src: 'imgs/alaska01.jpg', tooltip: 'Fairbanks', description: `The city is extremely far north, being located close to 16 parallels north of the Pacific border between the U.S. and Canada. It is roughly on the same parallel as the northern Swedish city of Skellefteå and Finnish city of Oulu. Apart from those cities, this parallel is sparsely populated due to its cold climate. On account of its warm summers, however, Fairbanks is located south of the arctic tree line.`},
    { src: 'imgs/alaska02.jpg', tooltip: 'Barrow', description: `Utqiaġvik (Inupiaq: [ut.qe.ɑʁ.βik]),[6] commonly known by its former name Barrow (/ˈbɛəroʊ/), is the largest city of the North Slope Borough in the U.S. state of Alaska and is located north of the Arctic Circle.[7][8] It is the 11th northernmost public community in the world and is the northernmost city in the United States. Nearby Point Barrow is the country's northernmost point. Barrow's population was 4,683 at the 2000 census and 4,212 at the 2010 census.`},
    { src: 'imgs/alaska03.jpg', tooltip: 'Anchorage', description: `Anchorage (officially called the Municipality of Anchorage) (Dena'ina Athabascan: Dgheyaytnu) is a unified home rule municipality in the U.S. state of Alaska. With an estimated 298,192 residents in 2016,[7] it is Alaska's most populous city and contains more than 40 percent of the state's total population; among the 50 states, only New York has a higher percentage of residents who live in its most populous city.`},
    { src: 'imgs/alaska04.jpg', tooltip: 'Valdez', description: `Valdez /vælˈdiːz/,/vəlˈdɛz/ (Alutiiq: Suacit) is a city in Valdez-Cordova Census Area in the U.S. state of Alaska. According to the 2010 US Census, the population of the city is 3,976. The city was named in 1790 after the Spanish Navy Minister Antonio Valdés y Fernández Bazán. A former Gold Rush town, it is located at the head of a fjord on the eastern side of Prince William Sound.`},
    { src: 'imgs/alaska05.jpg', tooltip: 'Bethel', description: `Bethel (Mamterilleq in Central Alaskan Yup'ik) is a city located near the west coast of the U.S. state of Alaska, approximately 400 miles (640 km) west of Anchorage, in the Bethel Census Area. Accessible only by air and river, Bethel is the main port on the Kuskokwim River and is an administrative and transportation hub for the 56 villages in the Yukon-Kuskokwim Delta.`},
    { src: 'imgs/alaska06.jpg', tooltip: 'Nome', description: `Nome (/ˈnoʊm/; Inupiaq: Siqnazuaq IPA: [siqnɐzuɑq]) is a city in the Nome Census Area in the Unorganized Borough of the U.S. state of Alaska. The city is located on the southern Seward Peninsula coast on Norton Sound of the Bering Sea. In 2014 the population was estimated at 3,788, a rise from the 3,598 recorded in the 2010 Census. `},
    { src: 'imgs/alaska07.jpg', tooltip: 'Kodiak', description: `Kodiak (Alutiiq: Sun'aq; Russian: Кадьяк, tr. Kadʹyak) is one of seven communities and the main city on Kodiak Island, Kodiak Island Borough, in the U.S. state of Alaska. All commercial transportation between the entire island and the outside world goes through this city either via ferryboat or airline. The population was 6,130 as of the 2010 census. 2014 estimates put the population at 6,304.`},
    { src: 'imgs/alaska08.jpg', tooltip: 'Prudhoe Bay', description: `Prudhoe Bay /ˈpruːdoʊ/ or Sagavanirktok[pronunciation?] is a census-designated place (CDP) located in North Slope Borough in the U.S. state of Alaska. As of the 2010 census, the population of the CDP was 2,174 people; however, at any given time several thousand transient workers support the Prudhoe Bay oil field. The airport, lodging, and general store are located at Deadhorse; the rigs and processing facilities are located on scattered gravel pads laid atop the tundra.`}
];

createMainElements();
createPictures(pics);

let picsList = document.querySelectorAll('.pic');
let buttonLeft = document.querySelector('.left');
let buttonRight = document.querySelector('.right');
let bigPic = document.querySelector('.bigPic');
let slideNumber = 0;

growingThumbs(slideNumber);

function onNavButtonClick(event) {
    normalThumbs(slideNumber);
    movePics(parseInt(event.target.getAttribute('data-direction'), 10));
}

function movePics(direction) {
    if (slideNumber === 0 && direction < 0) {
        changePic(picsList.length - 1);
    } else if (slideNumber === picsList.length - 1 && direction > 0) {
        changePic(0);
    } else {
        changePic(slideNumber + direction);
    }
    growingThumbs(slideNumber);
}

function growingThumbs(index) {
    let picture = document.querySelectorAll('.pic')[index];
    picture.className = 'pic grow';
}

function normalThumbs(index) {
    let picture = document.querySelectorAll('.pic')[index];
    picture.className = 'pic';
}

function createMainElements() {
    document.querySelector('main').innerHTML = `<div class="left button"><i data-direction="-1" class="fa fa-arrow-circle-left fa-3x" aria-hidden="true"></i></div>`
    document.querySelector('main').innerHTML += `<div class="mainPic"></div>`
    document.querySelector('main').innerHTML += `<div class="right button"><i data-direction="1" class="fa fa-arrow-circle-right fa-3x" aria-hidden="true"></i></div>`
}

function changePic(itemNum) {
    bigPic.setAttribute('style', picsList[itemNum].getAttribute('style'));
    document.querySelector('.bigPic').innerHTML = `<footer><h1>${pics[itemNum].tooltip}</h1><p>${pics[itemNum].description}</p></footer>`
    slideNumber = itemNum;
    growingThumbs(slideNumber);
}

function findPicsIndex(picSrc) {
    picsList.forEach(function (picture, index) {
        if (picture.getAttribute('src') === picSrc) {
            changePic(index);
        }
    });
}

picsList.forEach(function(picture) {
    picture.onclick = onPictureClick;
});

function onPictureClick(event) {
    document.documentElement.scrollTop = 0;
    normalThumbs(slideNumber);
    let picSrc = (event.target.getAttribute('src'));
    findPicsIndex(picSrc);
}

function createPictures(arrayOfPics) {
    document.querySelector('.mainPic').innerHTML = `<button class='bigPic' style='background-image: url(${arrayOfPics[0].src})' src='${arrayOfPics[0].src}' tooltip='${arrayOfPics[0].tooltip}'></button>`;
    document.querySelector('.bigPic').innerHTML = `<footer><h1>${pics[0].tooltip}</h1><p>${pics[0].description}</p></footer>`
    arrayOfPics.forEach(function (pic) {
        document.querySelector('section').innerHTML += `<button class='pic' style='background-image: url(${pic.src})' src='${pic.src}' tooltip='${pic.tooltip}'></button>`
    });
}

buttonLeft.onclick = onNavButtonClick;
buttonRight.onclick = onNavButtonClick;
