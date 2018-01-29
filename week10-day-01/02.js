'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectagles(sideA, sideB) {
  this.sideA = sideA;
  this.sideB = sideB;
}

Rectagles.prototype.getArea = function() {
    return this.sideA * this.sideB;
}

Rectagles.prototype.getCircumference = function() {
  return (this.sideA * 2) + (this.sideB * 2);
}

let rectangle = new Rectagles(10, 10);

console.log(rectangle.getArea());

console.log(rectangle.getCircumference());
