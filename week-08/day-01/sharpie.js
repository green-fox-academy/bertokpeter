function Sharpie(color, width) {
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
    this.use = function(){
        this.inkAmount -= this.width;
        if (this.inkAmount < 0) {
            this.inkAmount = 0;
        }
    };
}

let sharp = new Sharpie('red', 55);
while (sharp.inkAmount > 0) {
    sharp.use();
    console.log(sharp.inkAmount);
}