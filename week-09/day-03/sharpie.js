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
  if (typeof inkAmount !== 'number' || typeof width !== 'number') {
    throw new Error('error');
  }
  for (let i = inkAmount; i >= width; i -= width) {
    color.inkAmount -= color.width;
  }
  return `${color.color} ink amount left: ${color.inkAmount}`;
}

console.log(useSharpie(red, red.inkAmount, red.width));
console.log(useSharpie(yellow, yellow.inkAmount, yellow.width));

