'use strict';

let test = require('tape');
let appleClass = require('./apple.js');

test('concat strings', function (t) {  
    let apple = new appleClass();
    t.equal(apple.getApple(), 'appl');
    t.end();
});

test('summ array', function(t) {
    let apple = new appleClass();
    t.equal(apple.sum([1,2,3,4,5]), 15);
    t.end();
});

test('summ empty', function(t) {
    let apple = new appleClass();
    t.equal(apple.sum([]), 0);
    t.end();
});

test('summ one', function(t) {
    let apple = new appleClass();
    t.equal(apple.sum([5]), 5);
    t.end();
});

test('summ null', function(t) {
    let apple = new appleClass();
    t.equal(apple.sum(null), 0);
    t.end();
});

test('summ string', function(t) {
    let apple = new appleClass();
    t.error(apple.sum(null), 0);
    t.end();
});