'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

setTimeout(function(){
    print('melon');
}, 3000);
setTimeout(function(){
    print('grapes');
}, 5000);
setTimeout(function(){
    print('apple');
}, 1000);
print('pear');

function print(fruit){
    console.log(fruit);
}