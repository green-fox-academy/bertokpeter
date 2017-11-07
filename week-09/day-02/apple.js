'use strict';

class Apple {
    getApple() {
        return 'appl';
    }

    sum(numArray) {
        if (numArray === null || numArray.length === 0){
            numArray = [0];
        }
        let summa = numArray.reduce(function(sum, value) {
            return sum + value;
        });
        return summa;
    }
};

module.exports = Apple;