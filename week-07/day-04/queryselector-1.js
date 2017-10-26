let king = document.getElementById('b325');
console.log(king);

let conceited = document.querySelector('.b326');
alert(conceited);

let businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function(e){
    console.log(e);
});

let conceitedKing = document.querySelectorAll('.container div');
conceitedKing.forEach(function(e) {
    alert(e);
});

let noBusiness = document.querySelectorAll('div');
noBusiness.forEach(function(e){
    console.log(e);
});

let allBizniss = document.getElementsByTagName('p');
alert(allBizniss);
