const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += amt;
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += amt;
    }
}

const Shuffler = {
    cash: 10000,
    count: 0,
    pick: function() {
        this.cash -= 1000;
        let name = null;
        if (this.count % 2 == 0) {
            name = Panama;
        } else {
            name = Cyprus;
        }
        this.count += 1;
        name.deposit(1000);
        console.log(name.name + ' got 1000' );
    }
}

Shuffler.pick(Panama) // prints Panama got 1000
Shuffler.pick(Cyprus) // prints Cyprus got 1000
Shuffler.pick(Panama) // prints Panama got 1000
Shuffler.pick(Cyprus) // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 