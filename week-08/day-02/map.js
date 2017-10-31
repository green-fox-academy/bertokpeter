'use strict';

var fruits = [
	'melon',
	'apple',
	'strawberry',
	'blueberry',
	'pear',
	'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

function numberOfE(word) {
	let count = 0;
	for (let i = 0; i < word.length; i++) {
		if (word[i]==='e'){
			count++;
		}
	}
	return count;
}

let fruitEs = fruits.map(numberOfE);
console.log(fruitEs);