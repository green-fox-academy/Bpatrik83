'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

let girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
let boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
let order = [];

// order = girls.concat(boys);

for (let i = 0; i < girls.length; i++) {
    order.push(girls[i]);
    order.push(boys[i]);
}

console.log(order);
