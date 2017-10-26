'use strict';

const planetData = [
    {
      category: 'inhabited',
      content: 'Foxes',
      asteroid: true
    },
    {
      category: 'inhabited',
      content: 'Whales and Rabbits',
      asteroid: true
    },
    {
      category: 'uninhabited',
      content: 'Baobabs and Roses',
      asteroid: true
    },
    {
      category: 'inhabited',
      content: 'Giant monsters',
      asteroid: false
    },
    {
      category: 'inhabited',
      content: 'Sheep',
      asteroid: true
    }
  ]

let king = document.querySelector('.asteroids li');
let asteroids = document.querySelector('.asteroids');
asteroids.removeChild(king);

for (let i = 0; i < planetData.length; i++) {
    if (planetData[i].asteroid) {
        let item = document.createElement('li');
        item.classList.add(planetData[i].category)
        item.textContent = planetData[i].content;
        asteroids.appendChild(item);
    }
}