'use strict'

class Sharpie {

    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }
    use() {
        this.inkAmount -= this.width;
    }
}

let red = new Sharpie('red', 11);
let yellow = new Sharpie('yellow', 32);

function useSharpie(color, inkAmount, width) {
    for (let i = inkAmount; i >= width; i-= width) {
    color.inkAmount -= color.width;
        console.log(`${color.color} ink amount left: ${color.inkAmount}`);
    }
}

useSharpie(red, red.inkAmount, red.width);
useSharpie(yellow, yellow.inkAmount, yellow.width);
