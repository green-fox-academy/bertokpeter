'use strict';
let heading = document.querySelector('h1');

function display(){
    let code = event.keyCode;
    console.log(event);
    heading.textContent = "Last pressed key code is: " + code;
}

window.addEventListener('keyup', display);