'use strict';
// Create a function takes a string and a letter and splits the string to an list of strings by the letter
// like: "a,bcd,e,fg" and ',' becomes ["a", "bcd", "e", "fg"]

const stringSplitter = function(text, character) {
    let splittedStirng = [];
    let newString = '';
    for (let i=0; i < text.length; i++){
        if (text[i] === character){
            if (i > 0) {
                splittedStirng.push(newString);
                newString = '';
            }
        } else {
            newString += text[i]
        }
    }
    if (newString) {
        splittedStirng.push(newString);
    }
    return splittedStirng;
}

console.log(stringSplitter('ekerekperec', 'e'));

module.exports = stringSplitter;