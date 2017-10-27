'use strict';

let button = document.querySelector('button');
let div = document.querySelector('div');

button.addEventListener('click', changeBg);
function changeBg() {
        div.classList.toggle('party')
}
// function changeBg() {
//     if (div.classList.contains('party')){
//         div.classList.remove('party')
//     } else {
//         div.classList.add('party');
//     }
// }