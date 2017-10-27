'use strict';

let things = ['apple', 'banana', 'cat', 'dog'];
let items = document.getElementsByTagName('li');

for (let i = 0; i < items.length; i++) {
    items[i].textContent = things[i];
}

// items.forEach(function(e,i) {
//     e.textContent = things[i];
// });

// let ul = document.querySelector('ul');
// ul.style.backgroundColor = 'limegreen';
