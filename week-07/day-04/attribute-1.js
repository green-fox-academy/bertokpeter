'use strict';

let image = document.querySelector('img');
console.log(image.getAttribute('src'));
image.setAttribute('src', 'kroki.jpg');

let anchor = document.querySelector('a');
anchor.setAttribute('href', 'https://github.com/greenfox-academy/teaching-materials/tree/master/workshop/dom');

let button = document.querySelector('.this-one');
button.disabled = true;
button.textContent = 'Don\' t click me!';