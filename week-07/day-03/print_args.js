'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)
function printer(...string) {
    console.log(string.join(' '));
}

printer('hey', 'Peti', 'hey', 'Ati');