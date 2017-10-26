'use strict';

let things = ['apple', 'banana', 'cat', 'dog'];
let lis = document.querySelectorAll('li');

lis.forEach(function(e,i) {
    e.textContent = things[i];
});

let ul = document.querySelector('ul');
ul.style.backgroundColor = 'limegreen';
