'use strict';

const createCandy = document.querySelector('button.create-candies');
const candyCount = document.querySelector('dd.candies');
let candyNumber = 0;
createCandy.addEventListener('click',addCandy);

const buyLollypop = document.querySelector('button.buy-lollypops');
const lollypopCount = document.querySelector('dd.lollypops');
let lollypopNum = 0;
buyLollypop.addEventListener('click', addLollypop);

let CPS = document.querySelector('dd.speed');
let candySpeed = 0;
let multiplier = 1;
let candyGenerator = setInterval(function(){
    candyPerSecond(multiplier);
},1000);

const rainButton = document.querySelector('button.candy-machine');
rainButton.addEventListener('click', candyRain);

function addCandy(){
    candyNumber++;
    updateNumber();
}

function addLollypop(){
    if(candyCount.textContent >= 100){
        candyNumber -= 100;
        updateNumber();
        lollypopCount.textContent += "🍭";
        lollypopNum++;
        candySpeed += 1;
        CPS.textContent = candySpeed;
    }
}

function candyPerSecond(multiplier){
    candyNumber = candyNumber + lollypopNum*multiplier;
    updateNumber();
}

function updateNumber(){
    candyCount.textContent = candyNumber;
}

function candyRain(){
    multiplier *= 10;
    candySpeed *= 10;
    CPS.textContent = candySpeed;
}