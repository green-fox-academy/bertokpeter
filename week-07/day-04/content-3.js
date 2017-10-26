'use strict';

let firstp = document.querySelector('body > p');
let output1 = document.querySelector('.output1');
let output2 = document.querySelector('.output2');

output1.textContent = firstp.textContent;
output2.innerHTML = firstp.innerHTML;
