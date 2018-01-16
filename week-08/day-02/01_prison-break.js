// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

function prison(name) {
    let countVisit = 1;
    let fugitiveCount = 1;
    let fugitive = name;
    return {
        visit: function () {
            fugitiveCount > 0 ? console.log(`${fugitive} is visited ${countVisit} time(s)`) :
            console.log(`Nobody is here anymore`);
            countVisit++;
        },
        escape: function () {
            console.log(`BREAKING NEWS, ${fugitive} a escaped the prison`);
            fugitiveCount = 0;
        }
    }
}

const alcatraz = prison('Sad Panda');

alcatraz.visit(); // Sad Panda is visited 1 time(s)
alcatraz.visit(); // Sad Panda is visited 2 time(s)
alcatraz.escape(); // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit(); // Nobody is here anymore
