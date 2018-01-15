'use strict';

let test = require('tape');
let splitter = require('./final_exam');

test('simple string', function(t) {
    t.deepEqual(splitter("a,bcd,e,fg", ","),["a", "bcd", "e", "fg"]);
    t.end();
});

test('characters at the ends', function(t) {
    t.deepEqual(splitter("eszperente", "e"),["szp", "r", "nt"]);
    t.end();
});