'use strict';

let result = document.querySelector('.result');
let button = document.querySelector('button');
let items = document.querySelectorAll('li');

function countItems(){
    let count = items.length;
    result.textContent = count;
}

button.addEventListener('click', countItems);