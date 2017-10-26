'use strict';

let button = document.querySelector('button');
let bod = document.querySelector('body');
function changebg() {
    if (bod.classList.contains('party')){
        bod.classList.remove('party')
    } else {
        bod.classList.add('party');
    }
}

button.addEventListener('click', changebg);