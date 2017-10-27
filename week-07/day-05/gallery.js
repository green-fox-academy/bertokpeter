'use strict';

let images = [{'title': 'Yoda', 'description': 'Spiritual Leader of the Jedi Order. Yoda maybe small but no one knows more about the Force than him and only few can stand against his sword attacks.', 'url': 'images/yoda.jpg'}, 
              {'title': 'Mace Windu', 'description': 'Military Leader of the Jedi Order. Mace Windu is maybe the most powerful jedi. His fighting style involves mostly brutal Force-powered attacks.', 'url': 'images/mace_windu.jpg'},
              {'title': 'Obi-Wan', 'description': 'Jedi Master. After his padawan joined the Dark Side Obi-Wan banished himself to Tatooine for his failure. Powerful jedi master fighting Sith Lords countless times.', 'url': 'images/obi-wan.jpg'},
              {'title': 'Darth Maul', 'description': 'Sith Lord. Maul was maybe the most talented padawan of Sidious. An excellent sword fighter and with his two-bladed saber he can cut through most of his enemies.', 'url': 'images/Darth_Maul.jpg'},
              {'title': 'Darth Tyranus', 'description': 'Sith Lord a. k. a. Count Dooku. Dooku was once a jedi but Sidious lured him to the Dark Side.', 'url': 'images/Darth_Tyranus.jpg'},
              {'title': 'Darth Vader', 'description': 'Sith Lord. More machine than man, Vader betrayed his order and his master Obi-Wan and joined the Dark Side for more power.', 'url': 'images/Darth_Vader.jpg'},
              {'title': 'Darth Sidious', 'description': 'Lord of the Sith. He is the strongest among his kind and master of all Sith. A master of manipulating the Forece and with Force Lightning at his command, he is am ost formidable foe', 'url': 'images/darth_sidious.jpg'}
             ];

let container = document.querySelector('.container');
let navbar = document.querySelector('.navbar');
let image = document.querySelector('.image');

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
});

let left = document.querySelector('.left');
let right = document.querySelector('.right');

left.addEventListener('click', function(){
    changeImage('left');
});
right.addEventListener('click', function(){
    changeImage('right');
});

function changeImage(direction){
    let src = image.getAttribute('src')
    let index = getIndex(src)
    if (direction === 'left'){
        if (index === 0) {
            image.setAttribute('src', images[images.length-1].url);
        } else {
            image.setAttribute('src', images[index-1].url);
        }
    } else {
        if (index === images.length-1) {
            image.setAttribute('src', images[0].url);
        } else {
            image.setAttribute('src', images[index+1].url);
        }
    }
}

function getIndex(source) {
    for (let i = 0; i < images.length; i++) {
        if (images[i].url === source) {
            return i;
        }
    }
}