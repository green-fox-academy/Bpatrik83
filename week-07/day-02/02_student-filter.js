'use strict';

var students = [
    {'name': 'Rezso', 'age': 9.5, 'candies': 2},
    {'name': 'Gerzson', 'age': 10, 'candies': 1},
    {'name': 'Aurel', 'age': 7, 'candies': 3},
    {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs:
//  - how many candies they have on average

function whoHasGotMoreThanFourCandies(list) {
    let nameMoreFourCandies = [];
    students.map(student => student.candies > 4 ? nameMoreFourCandies.push(student.name) : 0);
    return nameMoreFourCandies;
}

console.log(whoHasGotMoreThanFourCandies(students));

function candiesAverageCounter(list) {
    let sumCandies = 0;
    students.map(student => sumCandies += student.candies);
    return sumCandies / students.length;
}

console.log(candiesAverageCounter(students));