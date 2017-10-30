function Sharpie(color, width) {
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
    this.use = function(){
        this.inkAmount -= this.width;
    };
}

let sharp = new Sharpie('red', 3);
while (sharp.inkAmount >= sharp.width) {
    sharp.use();
    console.log(sharp.inkAmount);
}