'use strict';
// Create a function that prints the ingredient list of dictionaries to the console in the following format:
//
// +--------------------+---------------+----------+
// | Ingredient         | Needs cooling | In stock |
// +--------------------+---------------+----------+
// | vodka              | Yes           | 1        |
// | coffee_liqueur     | Yes           | -        |
// | fresh_cream        | Yes           | 1        |
// | captain_morgan_rum | Yes           | 2        |
// | mint_leaves        | No            | -        |
// +--------------------+---------------+----------+
//
// OPTIONAL
// The frist columns should be automatically as wide as the longest key

const ingredients = [
    { "name": "vodka", "in_stock": 1, "needs_cooling": true },
    { "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": true },
    { "name": "fresh_cream", "in_stock": 10, "needs_cooling": true },
    { "name": "captain_morgan_rum_white", "in_stock": 2, "needs_cooling": true },
    { "name": "mint_leaves", "in_stock": 0, "needs_cooling": false },
    { "name": "sugar", "in_stock": 0, "needs_cooling": false },
    { "name": "lime juice", "in_stock": 0, "needs_cooling": true },
    { "name": "soda", "in_stock": 0, "needs_cooling": true }
];

let longestWord = function checkNameLength(list) {
    let longestWord = 12;
    ingredients.map(ingredient => ingredient.name.length > longestWord ? longestWord = ingredient.name.length : 0);
    return longestWord + 2;
}

function checkTrueOrFalse(logicValue) {
    if (logicValue === true) {
        return 'Yes'
    }
    return 'NO'
}

function changStockValue(stockNumber) {
    if (stockNumber === 0) {
        return '-'
    }
    return stockNumber
}

console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');
console.log('| ' + 'Ingredient' + ' '.repeat(longestWord() - 11) + '|' + ' Needs cooling ' + '|' + ' In stock ' + '|');
console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');
for (let i = 0; i < ingredients.length; i++) {
    console.log('| ' + ingredients[i].name + ' '.repeat(longestWord() - ingredients[i].name.length - 1) + '| '
        + checkTrueOrFalse(ingredients[i].needs_cooling) + ' '.repeat(14 - checkTrueOrFalse(ingredients[i].needs_cooling).length)
        + '| ' + changStockValue(ingredients[i].in_stock) + ' '.repeat(9 - ingredients[i].in_stock.toString( ).length) + '|');
}
console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');