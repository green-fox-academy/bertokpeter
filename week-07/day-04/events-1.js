'use strict';

let button = document.querySelector('button');
let bod = document.querySelector('div');

function changeBg() {
    bod.classList.toggle('party')
}

button.addEventListener('click', changeBg);
// function changebg() {
//     if (bod.classList.contains('party')){
//         bod.classList.remove('party')
//     } else {
//         bod.classList.add('party');
//     }
// }