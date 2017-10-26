'use strict';

let paragraphs = document.querySelectorAll('p');
if (paragraphs[2].classList.contains('red-dot')) {
    alert('OMG DOTS!');
}

if (paragraphs[3].classList.contains('dolphin')) {
    paragraphs[0].textContent = 'pear';
}

if (paragraphs[0].classList.contains('apple')) {
    paragraphs[2].textContent = 'dog';
}

paragraphs[0].classList.add('red');
paragraphs[1].classList.remove('balloon');