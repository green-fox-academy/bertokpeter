'use strict';

const kids = [{"pet_name":"Wattled crane","owner":"Bryant"},
              {"pet_name":"Devil, tasmanian","owner":"Alejandro"},
              {"pet_name":"Mynah, common","owner":"Nelie"},
              {"pet_name":"Dolphin, common","owner":"Mariele"},
              {"pet_name":"Gray duiker","owner":"Maddalena"},
              {"pet_name":"Crab (unidentified)","owner":"Lucine"},
              {"pet_name":"Ant (unidentified)","owner":"Lorianna"},
              {"pet_name":"Bison, american","owner":"Tommie"},
              {"pet_name":"Yellow mongoose","owner":"Vivyan"},
              {"pet_name":"Carpet snake","owner":"Veda"},
              {"pet_name":"Lesser mouse lemur","owner":"Isidor"}];

let pets = document.getElementById('pets');

kids.forEach(function(e){
    let article = document.createElement('article');
    let h3 = document.createElement('h3');
    let p = document.createElement('p');
    h3.textContent = e.owner;
    p.textContent = e.pet_name;
    pets.appendChild(article);
    article.appendChild(h3);
    article.appendChild(p);
});