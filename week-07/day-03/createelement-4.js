'use strict';

let petParent = document.getElementById('pets');

const kids = [{"pet_name":"Wattled crane","owner":"Bryant"},
    {"pet_name":"Devil, tasmanian","owner":"Alejandro"},
    {"pet_name":"Mynah, common","owner":"Nelie"},
    {"pet_name":"Dolphin, common","owner":"Mariele"},
    {"pet_name":"Gray duiker","owner":"Maddalena"},
    {"pet_name":"Crab (unidentified)","owner":"Lucine"},
    {"pet_name":"Ant (unidentified)","owner":"Lorianna"},
    {"pet_name":"Bison, american","owner":"Tommie"},
    {"pet_name":"Yellow mongoose","owner":"Vivyan"},
    {"pet_name":"Carpet snake","owner":"Veda"},
    {"pet_name":"Lesser mouse lemur","owner":"Isidor"}];

function createH3(owner) {
    let tempH3 = document.createElement('h3');
    tempH3.textContent = owner;
    return tempH3;
}

function createP(petName) {
    let tempP = document.createElement('p');
    tempP.textContent = petName;
    return tempP;
}

for (let i = 0; i < kids.length; i++) {
    let tempArticle = document.createElement('article');
    tempArticle.appendChild(createH3(kids[i].owner));
    tempArticle.appendChild(createP(kids[i].pet_name));
    petParent.appendChild(tempArticle);
}