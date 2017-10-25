'use strict';

let students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function got_more(student_log) {
    student_log.forEach(function(e) {
        if (e["candies"] > 4) {
            console.log(e["name"], "has more than 4 candies.");
        }
    });
}

got_more(students);

function average_candies(student_log) {
    let avr_candies = 0;
    student_log.forEach(function(e) {
        avr_candies += e["candies"];
    }); 
    avr_candies /= student_log.length;
    return avr_candies;
}

console.log(average_candies(students))