'use strict';

let heading = document.querySelector('h1');
alert(heading.textContent);

let firstp = document.querySelector('body > p');
console.log(firstp.textContent);

let secondp = document.querySelector('.other');
alert(secondp.textContent);

heading.innerHTML = 'New content';

let thirdp = document.querySelector('.result');
thirdp.innerHTML = firstp.innerHTML;
