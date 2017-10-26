'usestrict';

let asteroidList = document.querySelector('ul.asteroids');
let greenFox = document.createElement('li');
greenFox.textContent = 'The Green Fox';
asteroidList.appendChild(greenFox);

let lamplighter = document.createElement('li');
lamplighter.textContent = 'The Lamplighter';
asteroidList.appendChild(lamplighter);

let container = document.querySelector('div.container');
let heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM!';
container.appendChild(heading);
let image = document.createElement('img');
image.setAttribute('src', 'kroki.jpg');
container.appendChild(image);
