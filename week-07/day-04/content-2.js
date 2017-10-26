'use strict';
let paragraphs = document.querySelectorAll('p');
let lastp = document.querySelector('.dog');
paragraphs.forEach(function(e) {
    e.innerHTML = lastp.innerHTML;
});