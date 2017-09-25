class Station(object):
    def __init__(self):
        self.gas_amount = 500.0
    
    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity
        return self.gas_amount

class Car(object):
    def __init__(self):
        self.gas_amount = 0
        self.capacity = 100

Toyota = Car()
Mol = Station()
print(Mol.refill(Toyota))
print(Toyota.gas_amount)