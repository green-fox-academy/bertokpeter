'use strict';

let images = [{'title': 'Yoda', 'description': 'Spiritual Leader of the Jedi Order. Yoda maybe small but no one knows more about the Force than him and only few can stand against his sword attacks.', 'url': 'images/yoda.jpg'}, 
              {'title': 'Mace Windu', 'description': 'Military Leader of the Jedi Order. Mace Windu is maybe the most powerful jedi. His fighting style involves mostly brutal Force-powered attacks.', 'url': 'images/mace_windu.jpg'},
              {'title': 'Obi-Wan', 'description': 'Jedi Master. After his padawan joined the Dark Side Obi-Wan banished himself to Tatooine for his failure. Powerful jedi master fighting Sith Lords countless times.', 'url': 'images/obi-wan.jpg'},
              {'title': 'Darth Maul', 'description': 'Sith Lord. Maul was maybe the most talented padawan of Sidious. An excellent sword fighter and with his two-bladed saber he can cut through most of his enemies.', 'url': 'images/Darth_Maul.jpg'},
              {'title': 'Darth Tyranus', 'description': 'Sith Lord a. k. a. Count Dooku. Dooku was once a jedi but Sidious lured him to the Dark Side, to lead a Separatist Movement against the Republic, and to sow the seeds of destruction among the jedi.', 'url': 'images/Darth_Tyranus.jpg'},
              {'title': 'Darth Vader', 'description': 'Sith Lord. Once destined to be The Chosen One, Vader, known as Anakin Skywalker at the time, allowed his fears to overcome him. Anakin betrayed his order and his master Obi-Wan and joined the Dark Side for more power to try and save his loved ones. Now more machine than man, Vader only cares about the destruction of the infamous Rebels...or is there a way to reach his previous self inside him?', 'url': 'images/Darth_Vader.jpg'},
              {'title': 'Darth Sidious', 'description': 'Lord of the Sith. He is the strongest among his kind and master of all Sith. A master of manipulating the Force and with Force Lightning at his command, he is am ost formidable foe', 'url': 'images/darth_sidious.jpg'}
             ];

let container = document.querySelector('.container');
let navbar = document.querySelector('.navbar');
let image = document.querySelector('.image');

image.setAttribute('src', images[0].url);
let article = document.createElement('article');
article.classList.add('article');
let title = document.createElement('h1');
title.textContent = images[0].title;
let description = document.createElement('p');
description.textContent = images[0].description;
description.style.marginTop = '15px';
container.appendChild(article);
article.appendChild(title);
article.appendChild(description);

images.forEach(function(){
    let item = document.createElement('li');
    item.classList.add('thumbnails');
    navbar.appendChild(item);
});

let thumbnails = document.querySelectorAll('.thumbnails');

thumbnails.forEach(function(e, i){
    e.style.backgroundImage = 'url(' + images[i].url + ')';
    e.style.backgroundRepeat = 'no-repeat';
    e.style.backgroundSize = '90px';
    e.style.backgroundPosition = 'center';
    if (images[i].title === 'Darth Tyranus') {
        e.style.backgroundPosition = 'top';
    }
    e.addEventListener('click', function(){
        let index = getIndex();
        thumbnails[index].classList.remove('selected');
        changeImage(i);
    });
});

thumbnails[0].classList.add('selected');

let left = document.querySelector('.left');
let right = document.querySelector('.right');

left.addEventListener('click', function(){
    slideImage('left');
});
right.addEventListener('click', function(){
    slideImage('right');
});

function slideImage(direction){
    let index = getIndex();
    thumbnails[index].classList.remove('selected');
    if (direction === 'left'){
        if (index === 0) {
            changeImage(images.length-1);
        } else {
            changeImage(index-1);
        }
    } else {
        if (index === images.length-1) {
            changeImage(0);
        } else {
            changeImage(index+1);
        }
    }
}

function getIndex() {
    let src = image.getAttribute('src');
    for (let i = 0; i < images.length; i++) {
        if (images[i].url === src) {
            return i;
        }
    }
}

function changeImage (index) {
    image.setAttribute('src', images[index].url);
    title.textContent = images[index].title;
    description.textContent = images[index].description;
    thumbnails[index].classList.add('selected');
}
