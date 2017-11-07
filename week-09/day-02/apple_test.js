'use strict';

let test = require('tape');
let apple = require('./apple.js');

test('concat strings', function (t) {  
    t.equal(apple.getApple(), 'appl');
    t.end();
});