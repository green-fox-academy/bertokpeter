'use strict';

let mega = document.querySelector('.candyshop li');
let candyshop = document.querySelector('.candyshop');
candyshop.removeChild(mega);

for (let i=1; i < 17; i++) {
    let item = document.createElement('li');
    item.textContent = 'Empty box #' + i;
    candyshop.appendChild(item);
}

let items = document.querySelectorAll('li');
items.forEach(function(e){
    e.style.backgroundColor = 'red';
});
// getelementnel nem mukszik a foreach
// ha uj ures listat csinalok akkor abba nem tudok foreachel uj li elemeket csinalni
// for ciklus fog kelleni
// ha modositani akarom oket uj valtozot kell csinalni mert a li mostantol az utolso
// es ekkor meg egz forEach