'use strict';
// - Create a variable named `nimals`
//   with the following content: `["kuty", "macsk", "cic"]`
// - Add all elements an `"a"` at the end
// - try to use built in functions instead of loops

let nimals = ["kuty", "macsk", "cic"];

function appendAToTheEnd(array) {
    return array.map(animal => animal + 'a');
}

console.log(appendAToTheEnd(nimals));
